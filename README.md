# Home Lab Monitoring Dashboard

![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-backend-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-in%20development-orange) <br>

A full-stack home lab monitoring system built with Django, Python agents, SQL, and a JavaScript dashboard.


## System Architecture

```mermaid
flowchart LR

Server1[Server 1]
Server2[Server 2]
Server3[Server 3]

Agent[Monitoring Agent<br>Python + psutil]

API[Django REST API]

DB[(Metrics Database)]

Dashboard[Monitoring Dashboard]

Server1 --> Agent
Server2 --> Agent
Server3 --> Agent

Agent -->|Send Metrics| API
API --> DB
API --> Dashboard
```


## Features

- Monitor multiple servers in a home lab
- Collect system metrics (CPU, RAM, Disk usage)
- Store metrics in a centralized database
- REST API for metric ingestion
- Web dashboard for visualizing system performance
- Modular architecture for adding new monitoring agents

Future Features
- Real-time metric updates
- Alerting and notifications
- Server uptime monitoring
- Docker deployment

## Tech Stack

### Backend
- Python
- Django
- Django REST Framework

### Monitoring Agent
- Python
- psutil

### Frontend
- JavaScript
- HTML/CSS
- Chart.js

### Database
- SQLite (development)
- PostgreSQL (production ready)

### Tools
- Git
- GitHub

## Setup

### 1. Clone the Repository

git clone https://github.com/YOURUSERNAME/homelab-monitoring-dashboard.git  
cd homelab-monitoring-dashboard

### 2. Create a Virtual Environment

python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the Django Server

cd backend  
python manage.py runserver

The API will be available at:

http://127.0.0.1:8000

## Roadmap

### Phase 1 – Core Backend

- [x] Django monitoring API
  - [x] Create Django project
  - [x] Create `metrics` app
  - [x] Configure Django REST Framework

- [x] Server registration
  - [x] Create `Server` model
  - [x] Register model in Django admin
  - [x] Create `/api/servers` endpoint

- [x] Metrics ingestion endpoint
  - [x] Create `Metric` model
  - [x] Create `/api/metrics` API endpoint
  - [x] Store CPU, RAM, and disk usage metrics
  - [x] Connect models with database migrations


### Phase 2 – Monitoring Agent

- [ ] Python monitoring script
  - [ ] Create monitoring agent in `agent/`
  - [ ] Collect CPU usage
  - [ ] Collect RAM usage
  - [ ] Collect disk usage

- [ ] Automatic metric reporting
  - [ ] Send metrics to `/api/metrics`
  - [ ] Run reporting loop every few seconds
  - [ ] Configure server ID for agent


### Phase 3 – Dashboard

- [ ] Web dashboard UI
  - [ ] Create dashboard HTML page
  - [ ] Fetch metrics from API
  - [ ] Display server status

- [ ] CPU / RAM / Disk charts
  - [ ] Integrate Chart.js
  - [ ] Display historical metrics
  - [ ] Auto-refresh data

- [ ] Server overview page
  - [ ] List monitored servers
  - [ ] Show latest server metrics
  - [ ] Add server selection


### Phase 4 – Advanced Features

- [ ] Real-time monitoring
  - [ ] Add WebSocket support
  - [ ] Push live metrics to dashboard

- [ ] Alerting system
  - [ ] CPU threshold alerts
  - [ ] RAM threshold alerts
  - [ ] Email or notification alerts

- [ ] Authentication
  - [ ] Protect dashboard endpoints
  - [ ] Add user login system

- [ ] Docker deployment
  - [ ] Dockerfile for Django backend
  - [ ] Docker Compose configuration
  - [ ] Containerized deployment

## Screenshots

Screenshots of the monitoring dashboard will be added once the frontend is implemented.