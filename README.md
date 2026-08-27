# 🚀 DevOps Resume Site

Сайт-резюме DevOps инженера с полным циклом CI/CD и развертыванием в облаке.

![CI/CD](https://github.com/wa1nntt2/devops-resume/actions/workflows/ci-cd.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-28.2-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1.35-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 Описание

Pet-проект для отработки DevOps практик: от написания кода до автоматического деплоя в облако. Включает полный цикл — контейнеризация, оркестрация, CI/CD, мониторинг и IaC.

## 🛠 Стек технологий

| Категория | Инструменты |
|-----------|-------------|
| **Backend** | Python 3.12, Flask, Gunicorn |
| **Контейнеризация** | Docker, Docker Compose |
| **Оркестрация** | Kubernetes (minikube) |
| **CI/CD** | GitHub Actions |
| **Автоматизация** | Ansible |
| **Web-сервер** | Nginx (reverse proxy + HTTPS) |
| **Мониторинг** | Prometheus, Grafana, Node Exporter |
| **Облако** | Yandex Cloud |

## 🏗 Архитектура

```mermaid
graph LR
    A[GitHub] --> B[GitHub Actions]
    B --> C[Тесты]
    C --> D[Docker Build]
    D --> E[GHCR]
    D --> F[SSH Deploy]
    F --> G[Yandex Cloud VM]
    G --> H[Nginx :443]
    H --> I[Flask :5000]
    G --> J[Prometheus]
    J --> K[Grafana]

🚀 Быстрый старт
Локальный запуск
bash

# Docker
docker build -t devops-resume .
docker run -d -p 5000:5000 devops-resume

# Docker Compose
docker compose up -d

Kubernetes
bash

minikube start
kubectl apply -f k8s/
kubectl port-forward service/devops-resume-service 8080:80

☁️ Деплой в Yandex Cloud
bash

# Настройка сервера
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/setup-server.yml

# Деплой приложения
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/deploy.yml

# Настройка Nginx + HTTPS
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/nginx.yml

# Мониторинг
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/monitoring.yml

🔄 CI/CD Pipeline

При push в main:

    ✅ Test — pytest

    🐳 Build — Docker image

    📦 Push — GHCR

    🚀 Deploy — SSH на VM

📊 Мониторинг
Сервис	URL
Сайт	https://<IP>
Prometheus	http://<IP>:9090
Grafana	http://<IP>:3000
Node Exporter	http://<IP>:9100
📁 Структура проекта
text

devops-resume/
├── .github/workflows/     # CI/CD
├── ansible/               # Playbooks
├── k8s/                   # Kubernetes манифесты
├── monitoring/            # Prometheus + Grafana
├── static/                # CSS
├── templates/             # HTML
├── tests/                 # Pytest
├── app.py                 # Flask приложение
├── Dockerfile
├── docker-compose.yml
└── requirements.txt

👤 Автор

wa1nntt2 — DevOps Engineer

https://img.shields.io/badge/GitHub-wa1nntt2-black
https://img.shields.io/badge/Email-wa1nntt2%2540gmail.com-red
📝 License

MIT © 2026 wa1nntt2
text


Обнови файл:

```bash
cat > README.md << 'MARKDOWN'
# 🚀 DevOps Resume Site

Сайт-резюме DevOps инженера с полным циклом CI/CD и развертыванием в облаке.

## 📋 Описание

Pet-проект для отработки DevOps практик: от написания кода до автоматического деплоя в облако.

## 🛠 Стек технологий

| Категория | Инструменты |
|-----------|-------------|
| **Backend** | Python 3.12, Flask, Gunicorn |
| **Контейнеризация** | Docker, Docker Compose |
| **Оркестрация** | Kubernetes (minikube) |
| **CI/CD** | GitHub Actions |
| **Автоматизация** | Ansible |
| **Web-сервер** | Nginx (reverse proxy + HTTPS) |
| **Мониторинг** | Prometheus, Grafana, Node Exporter |
| **Облако** | Yandex Cloud |

## 🚀 Быстрый старт

### Локальный запуск
```bash
docker build -t devops-resume .
docker run -d -p 5000:5000 devops-resume

Kubernetes
bash

minikube start
kubectl apply -f k8s/

☁️ Деплой в Yandex Cloud
bash

ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/setup-server.yml
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/deploy.yml
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/nginx.yml
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/monitoring.yml

🔄 CI/CD

При push в main: тесты → сборка → push в GHCR → деплой на VM
📊 Мониторинг
Сервис	URL
Сайт	https://<IP>
Prometheus	http://<IP>:9090
Grafana	http://<IP>:3000
👤 Автор

wa1nntt2 — DevOps Engineer

GitHub: wa1nntt2
Email: wa1nntt2@gmail.com