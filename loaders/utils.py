from pathlib import Path

from loaders.config import DIMENSION_PATH
from loaders.config import FACT_PATH


def get_dimension_file(filename: str) -> Path:

    return DIMENSION_PATH / filename


def get_fact_file(filename: str) -> Path:

    return FACT_PATH / filename