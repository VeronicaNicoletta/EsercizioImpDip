import psycopg2

def update_department(deptno, dname, loc):
    """ update department name based on the department id """
    sql = """ UPDATE dept
                SET dname = %s, loc=%s
                WHERE deptno = %d"""
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Vera@")
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (deptno, dname, loc,))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    # Update employee id 1
    update_department(56, "Matematica", "Roma")