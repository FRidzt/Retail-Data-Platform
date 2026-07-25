from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

RAW_DATASET_DIR = ROOT_DIR / "datasets" / "raw" / "dimension"


def ensure_directory():
    RAW_DATASET_DIR.mkdir(parents=True, exist_ok=True)


def get_output_file(filename: str):
    ensure_directory()
    return RAW_DATASET_DIR / filename