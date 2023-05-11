import psycopg2

import connection
from connection import connect
from department import Department


class DepartmentGateway:
    @staticmethod
    def insert_department(dept: Department):
        sql = """INSERT INTO dept(deptno, dname, loc)
                     VALUES(%s,%s,%s) RETURNING deptno, dname, loc"""
        conn = None
        try:
            conn=connection.connect()
            cur=conn.cursor()
            cur.execute(sql,(dept.deptno,dept.dname,dept.loc))
            row = cur.fetchone()
            print(row)
            conn.commit()
            cur.close()
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()

    @staticmethod
    def search_department(name: str):
        sql = "SELECT * FROM dept WHERE dname LIKE '%{}%'".format(name)
        conn = None
        try:
            conn = connection.connect()
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
            print(row)
            conn.commit()
            return True

        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()
        return False

    @staticmethod
    def update_department(id: int, dept: Department):
        sql = """ UPDATE dept
                            SET dname = %s, loc=%s
                            WHERE id = %d"""
        conn = None
        updated_rows = 0
        try:
            conn = connection.connect()
            cur = conn.cursor()
            cur.execute(sql, (id, dept.dname, dept.loc))
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
    def delete_department(id):
        sql = """DELETE FROM dept WHERE id = %s;"""
        conn = None
        rows_deleted = 0
        try:
            conn = connection.connect()
            conn = psycopg2.connect(conn)
            cur = conn.cursor()
            cur.execute(sql, (id,))
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
    def get_by_name_department():
        rows = []
        sql = "SELECT * FROM dept ORDER BY dname"
        conn = None
        try:
            conn = connection.connect()
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