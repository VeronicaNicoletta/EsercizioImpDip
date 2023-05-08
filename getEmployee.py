import psycopg2
import os

def get_employee():
    """ query data from the emp table """
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DATABASE_HOST"),
            database="postgres",
            user="postgres",
            password="Vera@")
        cur = conn.cursor()
        cur.execute("SELECT * FROM emp ORDER BY ename")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_employee()
    print(os.environ.get("DATABASE_HOST"))