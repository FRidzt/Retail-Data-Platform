from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

# Base Dataset Folder
DATASET_DIR = ROOT_DIR / "datasets"

# Layer
RAW_DATASET_DIR = DATASET_DIR / "raw"
BRONZE_DATASET_DIR = DATASET_DIR / "bronze"
SILVER_DATASET_DIR = DATASET_DIR / "silver"
GOLD_DATASET_DIR = DATASET_DIR / "gold"

# Raw Sub Folder
RAW_DIMENSION_DIR = RAW_DATASET_DIR / "dimension"
RAW_FACT_DIR = RAW_DATASET_DIR / "fact"


def ensure_directory():
    RAW_DIMENSION_DIR.mkdir(parents=True, exist_ok=True)
    RAW_FACT_DIR.mkdir(parents=True, exist_ok=True)


def get_output_file(filename: str):
    """
    Default output ke datasets/raw/dimension
    """
    ensure_directory()
    return RAW_DIMENSION_DIR / filename


def get_dimension_file(filename: str):
    """
    Membaca file dimension yang sudah dibuat
    """
    return RAW_DIMENSION_DIR / filename


def get_fact_file(filename: str):
    """
    Membaca atau menyimpan file fact
    """
    ensure_directory()
    return RAW_FACT_DIR / filename