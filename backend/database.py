import os
from typing import Any

import pymysql
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return pymysql.connect(
        host=os.getenv("DORIS_HOST", "127.0.0.1"),
        port=int(os.getenv("DORIS_PORT", "9030")),
        user=os.getenv("DORIS_USER", "root"),
        password=os.getenv("DORIS_PASSWORD", ""),
        database=os.getenv("DORIS_DATABASE", "taller3_analitica"),
        cursorclass=pymysql.cursors.DictCursor,
    )


def execute_query(query: str, params: tuple[Any, ...] = ()):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    finally:
        connection.close()
