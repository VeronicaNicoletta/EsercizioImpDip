import psycopg2

import employee
from connection import connect

from employee import Employee

class EmployeeGateway:
    @staticmethod
    def search_employee(name:str):
        sql = "SELECT * FROM emp WHERE ename LIKE '%{}%'".format(name)
        conn=None
        try:
            conn=connect()
            cur=conn.cursor()
            cur.execute(sql)
            row=cur.fetchone()
            print(row)
            conn.commit()

            cur.close()

        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()

    @staticmethod
    def insert_employee(emp:Employee):
        sql = """INSERT INTO emp(id, ename, job, mgr, hiredate, sal, comm, deptno)
                 VALUES(%d,%s,%s,%d,%s,%d,%d,%d) RETURNING id, ename, job, mgr, hiredate, sal, comm, deptno;"""
        conn = None
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute(sql, (emp.id, emp.ename, emp.job, emp.mgr, emp.hiredate, emp.sal, emp.comm, emp.deptno,))
            row = cur.fetchone()
            print(row)
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()



    @staticmethod
    def update_employee(id:int,emp:Employee):
        sql = """ UPDATE emp
                        SET ename = %s, job=%s, mgr=%s, hiredate=%s, sal=%s, comm=%s
                        WHERE id = %d"""
        conn = None
        updated_rows = 0
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute(sql, (id, emp.ename, emp.job,emp.mgr, emp.hiredate, emp.sal, emp.comm))
            updated_rows = cur.rowcount
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return updated_rows

    @staticmethod
    def delete_employee(id_emp):
        sql = """DELETE FROM emp WHERE id = %s;"""
        conn = None
        rows_deleted = 0
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute(sql, (id_emp,))
            rows_deleted = cur.rowcount
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return rows_deleted

    @staticmethod
    def get_by_name_employee():
        rows=[]
        sql="SELECT * FROM emp ORDER BY ename"
        conn = None
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute(sql)
            print("The number of parts: ", cur.rowcount)
            row = cur.fetchone()

            while row is not None:
                print(row)
                rows.append(row)
                row = cur.fetchone()
            cur.close()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


print(EmployeeGateway.get_by_name_employee())


