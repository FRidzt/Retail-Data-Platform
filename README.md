# Retail Data Platform

## Overview

End-to-End Modern Data Engineering Portfolio Project.

## Technology Stack

- Docker
- PostgreSQL
- Apache Airflow
- Apache Spark
- dbt
- Power BI
- Python
- Git & GitHub

## Architecture

Retail CSV Files
                               │
                               ▼
                     Python Data Generator
                               │
                               ▼
                    PostgreSQL (Raw Layer)
                               │
                               ▼
                         Apache Airflow
                     (Pipeline Orchestration)
                               │
                               ▼
                          Apache Spark
                  Cleaning & Transformation
                               │
                               ▼
                 PostgreSQL Warehouse
          Bronze → Silver → Gold Layer
                               │
                               ▼
                              dbt
        Star Schema + Data Quality + Documentation
                               │
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼
   Data Analyst          Power BI Dashboard     Data Science
         │                     │                     │
         └─────────────────────┴─────────────────────┘
                               │
                               ▼
                        Business Decision


## Project Status

🚧 Sprint 1 - Environment Setup