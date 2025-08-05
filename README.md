# Deep-Drift-Detection
This project provides a comprehensive framework to detect data drift and concept drift in deployed machine learning systems. Includes logging, alerting, and retraining triggers.

## Features
- Drift metrics using `evidently`
- Model explainability via SHAP
- Data pipeline integration using Apache Airflow
- Slack/Email alert notifications on drift

## Tech Stack
- Python, PyTorch
- Evidently AI, SHAP
- Apache Airflow, SQL

## Usage
```bash
python main.py
```

## Business Value
Avoid model decay and maintain high model accuracy over time in production environments.
