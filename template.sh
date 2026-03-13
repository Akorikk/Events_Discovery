#!/bin/bash

mkdir -p backend/api
mkdir -p backend/crawler
mkdir -p backend/extractor
mkdir -p backend/database
mkdir -p backend/services
mkdir -p backend/scheduler
mkdir -p frontend
mkdir -p scripts

touch backend/main.py
touch backend/api/routes.py

touch backend/crawler/crawler_manager.py
touch backend/crawler/heilbronn_crawler.py
touch backend/crawler/instagram_crawler.py

touch backend/extractor/event_extractor.py

touch backend/database/db.py
touch backend/database/models.py

touch backend/services/deduplicator.py
touch backend/services/webhook_service.py

touch backend/scheduler/scheduler.py

touch frontend/streamlit_app.py

touch requirements.txt
touch README.md
touch .env

echo "Project structure created successfully!"