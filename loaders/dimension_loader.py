from loaders.base_loader import BaseLoader

from loaders.logger import logger
from loaders.utils import get_dimension_file


class DimensionLoader(BaseLoader):

    def __init__(self):

        super().__init__("bronze")

    def load_table(self, table_name):

        csv_file = get_dimension_file(
            f"{table_name}.csv"
        )

        logger.info(
            f"Loading {csv_file.name}"
        )

        self.load_csv(
            table_name,
            csv_file,
            truncate=True
        )

        logger.info(
            f"{table_name} loaded successfully"
        )