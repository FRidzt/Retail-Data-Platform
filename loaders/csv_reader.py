from pathlib import Path

import pandas as pd

from loaders.validator import (
    validate_file,
    validate_dataframe,
)


def read_csv(file_path: Path):

    validate_file(file_path)

    dataframe = pd.read_csv(file_path)

    validate_dataframe(dataframe)

    return dataframe