import psycopg2


def connect():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Vera@")

    return conn
