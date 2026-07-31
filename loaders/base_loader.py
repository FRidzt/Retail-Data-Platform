from psycopg2.extras import execute_values

from loaders.csv_reader import read_csv
from loaders.database import Database


class BaseLoader:

    def __init__(self, schema="bronze"):

        self.schema = schema
        self.db = Database()

    # ==========================================
    # Truncate Table
    # ==========================================
    def truncate_table(self, table_name):

        sql = f"""
        TRUNCATE TABLE {self.schema}.{table_name}
        RESTART IDENTITY CASCADE;
        """

        self.db.execute(sql)
        self.db.commit()

    # ==========================================
    # Load DataFrame
    # ==========================================
    def load_dataframe(
        self,
        table_name,
        dataframe,
        truncate=False
    ):

        try:

            if truncate:
                self.truncate_table(table_name)

            columns = list(dataframe.columns)

            dataframe = dataframe.astype(object).where(
                dataframe.notna(),
                None
            )

            values = [
                tuple(row)
                for row in dataframe.to_numpy()
            ]

            sql = f"""
            INSERT INTO {self.schema}.{table_name}
            ({",".join(columns)})
            VALUES %s
            """

            execute_values(
                self.db.cursor,
                sql,
                values,
                page_size=1000
            )

            self.db.commit()

        except Exception as e:

            self.db.rollback()

            print()

            print("=" * 70)

            print(f"Failed loading table : {table_name}")

            print(e)

            print("=" * 70)

            raise

    # ==========================================
    # Load CSV
    # ==========================================
    def load_csv(
        self,
        table_name,
        csv_path,
        truncate=False
    ):

        dataframe = read_csv(csv_path)

        self.load_dataframe(
            table_name=table_name,
            dataframe=dataframe,
            truncate=truncate
        )

    # ==========================================
    # Close Connection
    # ==========================================
    def close(self):

        self.db.close()