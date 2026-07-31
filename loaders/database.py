import psycopg2

from loaders.config import DB_CONFIG
from loaders.logger import logger


class Database:

    def __init__(self):

        self.connection = psycopg2.connect(**DB_CONFIG)

        self.cursor = self.connection.cursor()

        logger.info("Connected to PostgreSQL")

    def execute(self, sql, params=None):

        self.cursor.execute(sql, params)

    def executemany(self, sql, params):

        self.cursor.executemany(sql, params)

    def fetchall(self):

        return self.cursor.fetchall()

    def fetchone(self):

        return self.cursor.fetchone()

    def commit(self):

        self.connection.commit()

    def rollback(self):

        self.connection.rollback()

    def close(self):

        self.cursor.close()

        self.connection.close()

        logger.info("Connection Closed")