DevOps Resume Site
Сайт-резюме DevOps инженера с полным циклом CI/CD и развертыванием в облаке.

Стек технологий
Backend: Python, Flask, Gunicorn

Контейнеризация: Docker, Docker Compose

Оркестрация: Kubernetes (minikube)

CI/CD: GitHub Actions

Автоматизация: Ansible

Web-сервер: Nginx (reverse proxy + HTTPS)

Мониторинг: Prometheus, Grafana, Node Exporter

Облако: Yandex Cloud

Архитектура
text
GitHub → GitHub Actions → Docker Build → GHCR
                                    ↓
                              SSH Deploy
                                    ↓
Yandex Cloud VM (Nginx → Flask → Gunicorn)
                                    ↓
                        Prometheus → Grafana
Локальная разработка
Запуск через Docker:
bash
docker build -t devops-resume:latest .
docker run -d --name devops-resume -p 5000:5000 devops-resume:latest
Запуск через Docker Compose:
bash
docker-compose up -d
Запуск в Kubernetes (minikube):
bash
minikube start
kubectl apply -f k8s/
kubectl port-forward service/devops-resume-service 8080:80
Деплой в Yandex Cloud
Настройка сервера:
bash
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/setup-server.yml
Деплой приложения:
bash
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/deploy.yml
Настройка Nginx:
bash
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/nginx.yml
Настройка мониторинга:
bash
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/monitoring.yml
CI/CD
При push в main автоматически:

Запускаются тесты (pytest)

Собирается Docker образ

Образ пушится в GHCR

Происходит деплой на VM через SSH

Мониторинг
Prometheus: http://<IP>:9090

Grafana: http://<IP>:3000

Node Exporter: http://<IP>:9100

Автор
wa1nntt2 — DevOps Engineer

GitHub: wa1nntt2

Email: wa1nntt2@gmail.com
