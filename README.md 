![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-Backend-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![Redis](https://img.shields.io/badge/Redis-7-red)
![Celery](https://img.shields.io/badge/Celery-Async-success)
![Status](https://img.shields.io/badge/status-Development-orange)

# 🚀 Basis Lead System

Multi-service Lead Management backend built with Django, PostgreSQL, Redis and Celery.

---

## 📌 Overview

Basis Lead System collects leads via Telegram bot, processes them asynchronously and displays results in a web dashboard.

The project demonstrates scalable backend architecture using service separation and containerization.

---

## 🧱 Architecture

The system is split into independent services:

- **bot** — Telegram bot (aiogram)
- **web** — Django app served by Gunicorn
- **db** — PostgreSQL database
- **redis** — message broker
- **celery** — background task worker

All services run inside Docker containers and communicate through an internal network.

---

## ⚙ Tech Stack

- Python 3.12
- Django
- PostgreSQL 15
- Redis 7
- Celery
- Gunicorn
- Docker / Docker Compose
- aiogram

---

## 🔥 Features

- Telegram lead collection
- Hot lead detection
- Async background processing
- PostgreSQL production database
- Dockerized architecture

---

## 🐳 Run Locally

```bash
docker-compose up --build

Open:http://localhost:8000
🔐 Environment Variables

Create .env based on .env.example:
SECRET_KEY=your_secret_key
POSTGRES_DB=your_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
BOT_TOKEN=your_bot_token
ADMIN_ID=your_admin_id

📦 Architectural Decisions

Celery used for asynchronous processing

Redis used as message broker

PostgreSQL selected for reliability and transactions

Service separation improves scalability and maintainability

Docker ensures consistent environment

📈 Future Improvements

REST API layer

JWT authentication

CI/CD integration

Kubernetes deployment

SaaS multi-tenant support

👨‍💻 Author

Backend architecture project focused on scalable system design and async processing.

