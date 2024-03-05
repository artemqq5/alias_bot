import pymysql

from data.config import PASSWORD_DATABASE, NAME_DATABASE


class DefaultDataBase:
    def __init__(self):
        self._connection = pymysql.connect(
            host="localhost",
            user="root",
            port=3306,
            autocommit=True,
            password=PASSWORD_DATABASE,
            db=NAME_DATABASE,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )

    def _insert(self, query, args=None):
        try:
            with self._connection as con:
                with con.cursor() as cursor:
                    return cursor.execute(query, args)
        except Exception as e:
            print(f"_insert: {e}")

    def _update(self, query, args=None):
        try:
            with self._connection as con:
                with con.cursor() as cursor:
                    return cursor.execute(query, args)
        except Exception as e:
            print(f"_update: {e}")

    def _delete(self, query, args=None):
        try:
            with self._connection as con:
                with con.cursor() as cursor:
                    return cursor.execute(query, args)
        except Exception as e:
            print(f"_delete: {e}")

    def _select(self, query, args=None):
        try:
            with self._connection as con:
                with con.cursor() as cursor:
                    cursor.execute(query, args)
                    return cursor.fetchall()
        except Exception as e:
            print(f"_select_all: {e}")

    def _select_one(self, query, args=None):
        try:
            with self._connection as con:
                with con.cursor() as cursor:
                    cursor.execute(query, args)
                    return cursor.fetchone()
        except Exception as e:
            print(f"_select_all: {e}")
