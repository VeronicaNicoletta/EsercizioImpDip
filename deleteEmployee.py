import psycopg2

def delete_employee(id):
    """ delete part by part id """
    sql= """DELETE FROM emp WHERE id = %s;"""
    conn = None
    rows_deleted = 0
    try:
        # read database configuration
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="")
        # connect to the PostgreSQL database
        conn = psycopg2.connect(conn)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM emp WHERE id = %s", (id,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted

if __name__ == '__main__':
    deleted_rows = delete_employee(25)
    print('The number of deleted rows: ', deleted_rows)