from pathlib import Path

import pandas as pd


def validate_file(filepath: Path):

    if not filepath.exists():

        raise FileNotFoundError(
            f"\nDataset tidak ditemukan:\n{filepath}"
        )

    if filepath.stat().st_size == 0:

        raise ValueError(
            f"\nDataset kosong:\n{filepath}"
        )


def validate_dataframe(df: pd.DataFrame):

    if df.empty:

        raise ValueError(
            "\nCSV tidak memiliki data."
        )

    if len(df.columns) == 0:

        raise ValueError(
            "\nCSV tidak memiliki header."
        )