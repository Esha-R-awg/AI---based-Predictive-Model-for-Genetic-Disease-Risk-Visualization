# Genetic Disease Risk Prediction Dashboard

## Overview
A full-stack app that:
1. Loads four Excel GWAS files.
2. Preprocesses & trains an XGBoost classifier.
3. Serves a FastAPI backend for predictions & logs to PostgreSQL.
4. Provides a React + Plotly front-end.

## Prerequisites
- Python 3.9+
- Node.js 14+
- Docker & docker-compose

## Setup

### 1. Launch PostgreSQL
```bash
cd db
docker-compose up -d
# then psql into it and run backend/database/init.sql
