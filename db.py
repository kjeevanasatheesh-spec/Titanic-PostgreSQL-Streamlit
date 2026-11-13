import pandas as pd
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="titanic_db",
        user="postgres",
        password="sbj@1975",
        port="5432",
        options="-c search_path=titanic_project,public"
    )

def run_query(sql):
    conn = get_connection()
    try:
        return pd.read_sql_query(sql, conn)
    finally:
        conn.close()