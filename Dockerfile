# === Этап 1: Сборка зависимостей ===
FROM python:3.12-slim AS builder

WORKDIR /app

# Ставим gcc и зависимости для пакетов с C-компиляцией
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Создаем виртуальное окружение
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# === Этап 2: Финальный минимальный образ ===
FROM python:3.12-slim

LABEL maintainer="wa1nntt2" \
      version="1.0" \
      description="DevOps Resume Site - Flask application"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Создаем пользователя
RUN useradd -m appuser

# Копируем виртуальное окружение из builder
COPY --from=builder /opt/venv /opt/venv

# Копируем код приложения
COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]