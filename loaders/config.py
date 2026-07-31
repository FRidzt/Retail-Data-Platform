from pathlib import Path

# =====================================
# PostgreSQL
# =====================================

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "retail_dw",
    "user": "postgres",
    "password": "postgres",
}

# =====================================
# Project
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_ROOT = PROJECT_ROOT / "datasets" / "raw"

DIMENSION_PATH = DATASET_ROOT / "dimension"

FACT_PATH = DATASET_ROOT / "fact"