import pymysql
from pymysql import cursors

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",    # ← Заменить на ваш реальный пароль
        database="hr_integration",           # ← Название БД из hr_integration.sql
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
        port=3310
    )
