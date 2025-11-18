import psycopg2
from psycopg2.extras import DictCursor

def select_dt():
    try:
        link = psycopg2.connect(
            user='admingonji',
            password='admingonji30032024',
            host='localhost',
            database='ct526'
            )

        cursor = link.cursor(cursor_factory=DictCursor)
        cursor.execute("SELECT * FROM movie;")
        
        dt = []
        dt = cursor.fetchall()

    except psycopg2.Error as e:
        
        return None

    finally:

        if cursor:
            cursor.close()
        if link:
            link.close()

        return dt

