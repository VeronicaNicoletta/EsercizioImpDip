import psycopg2


def insert_department(deptno, dname, loc):
    """ insert a new department into the dept table """
    sql = """INSERT INTO dept(deptno, dname, loc)
             VALUES(%d,%s,%s) RETURNING deptno, dname, loc;"""
    conn = None
    employee_id = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (deptno, dname, loc,))
        # get the generated id back
        employee_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return employee_id


if __name__ == '__main__':
    print(insert_department(43, 'Sviluppatrice', 'Cosenza'))