from db.db import get_connection

def get_all_employees():
    """
    Возвращает список всех сотрудников с указанием названия профессии.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    e.id,
                    e.full_name,
                    e.birth_date,
                    p.name AS profession,
                    e.status
                FROM employees e
                LEFT JOIN professions p ON e.profession_id = p.id
            """)
            return cursor.fetchall()
    finally:
        connection.close()


def get_all_professions():
    """
    Возвращает список всех профессий.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM professions")
            return cursor.fetchall()
    finally:
        connection.close()


def add_employee(full_name, birth_date, profession_id, created_by):
    """
    Добавляет нового сотрудника.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO employees (full_name, birth_date, profession_id, status, created_by)
                VALUES (%s, %s, %s, 'active', %s)
            """, (full_name, birth_date, profession_id, created_by))
    finally:
        connection.close()


def get_employee_by_id(emp_id):
    """
    Возвращает одного сотрудника по его ID.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, full_name, birth_date, profession_id
                FROM employees
                WHERE id = %s
            """, (emp_id,))
            return cursor.fetchone()
    finally:
        connection.close()


def update_employee(emp_id, full_name, birth_date, profession_id):
    """
    Обновляет данные сотрудника.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE employees
                SET full_name = %s,
                    birth_date = %s,
                    profession_id = %s
                WHERE id = %s
            """, (full_name, birth_date, profession_id, emp_id))
    finally:
        connection.close()


def fire_employee(emp_id):
    """
    Меняет статус сотрудника на 'inactive' (уволен).
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE employees
                SET status = 'inactive'
                WHERE id = %s
            """, (emp_id,))
    finally:
        connection.close()
