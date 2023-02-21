import os

import dotenv
import sqlite3
from singleton import Singleton


class DBConnection(metaclass=Singleton):
    """
    Technical class to open only one connection to the DB.
    """
    def __init__(self):
        dotenv.load_dotenv(override=True)
        # Open the connection. 
        self.__connection = sqlite3.connect(":memory:")
        self.__connection.row_factory = sqlite3.Row
        with open("init_db.sql", mode="r", encoding="utf8") as init_db:
            requests = init_db.read()
        self.__connection.cursor().executescript(requests)

    @property
    def cursor(self):
        """
        return the opened connection.

        :return: the opened connection.
        """
        return self.__connection.cursor()