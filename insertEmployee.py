import psycopg2


def insert_employee(id, ename, job, mgr, hiredate, sal, comm, deptno):
    """ insert a new employee into the emp table """
    sql = """INSERT INTO emp(id, ename, job, mgr, hiredate, sal, comm, deptno)
             VALUES(%d,%s,%s,%d,%s,%d,%d,%d) RETURNING id, ename, job, mgr, hiredate, sal, comm, deptno;"""
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
        cur.execute(sql, (id, ename, job, mgr, hiredate, sal, comm, deptno,))
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
    print(insert_employee(25, 'Veronica', 'Sviluppatrice', 7856, '05-05-2023', 2500, 400, 10))