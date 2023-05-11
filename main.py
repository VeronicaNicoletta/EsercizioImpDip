import department
import department_gateway
import employee
import employee_gateway
from employee_gateway import EmployeeGateway
def menu():
        print("\nWelcome\n")
        print("Do your choice...\n")
        print("[1] Create Employee")
        print("[2] Search Employee")
        print("[3] Get Employee")
        print("[4] Delete Employee")
        print("[5] Create Department")
        print("[6] Search Department")
        print("[7] Get Department")
        print("[8] Delete Department")
        print("[9] Esci")
        scelta = int(input("Insert your choice: "))
        if scelta==1:
            create_employee()
        elif scelta==2:
            name=input("Insert name:")
            employee_gateway.EmployeeGateway.search_employee(name)
        elif scelta==3:
            print("The Employee are:")
            employee_gateway.EmployeeGateway.get_by_name_employee()
        elif scelta==4:
            delete_employee()
        elif scelta==5:
            create_department()
        elif scelta==6:
            name = input("Insert name:")
            department_gateway.DepartmentGateway.search_department(name)
        elif scelta==7:
            print("The Departments are:")
            department_gateway.DepartmentGateway.get_by_name_department()
        elif scelta==8:
            delete_department()
        esc = input("Do you want exit? Insert 9 ")
        if esc == '9':
            print("Goodbye!")
            exit(0)
        else:
            print("Invalid choice...")
            menu()



def delete_department():
    department_gateway.DepartmentGateway.get_by_name_department()
    id_dept = input("Insert th id that you want delete: ")
    if id_dept.isnumeric():
        id_emp = int(id_dept)
        rows = department_gateway.DepartmentGateway.get_by_name_department()
        for row in rows:
            if id_dept in row:
                department_gateway.DepartmentGateway.delete_department(id_dept)
                print("Delete successfully")
            print("The entered id is wrong. Try again")



def create_department():
    print("Insert tuple into the table dept(deptno,dname,loc). Digit  0 to exit...")
    deptno=input("Inser deptno: ")
    dname=input("Insert deoartment name: ")
    loc=input("insert location: ")
    new_department=department.Department(deptno,dname,loc)
    department_gateway.DepartmentGateway.insert_department(new_department)


def delete_employee():
    employee_gateway.EmployeeGateway.get_by_name_employee()
    id_emp= input("Insert th id that you want delete: ")
    if id_emp.isnumeric():
        id_emp=int(id_emp)
        rows=employee_gateway.EmployeeGateway.get_by_name_employee()
        for row in rows:
            if id_emp in row:
                employee_gateway.EmployeeGateway.delete_employee(id_emp)
                print("Delete successfully")
            print("The entered id is wrong. Try again")





def create_employee():
    print("Insert tuple into the tables employee(id, ename, job, mgr, hiredate, sal, comm, deptno). Digit 0 to exit...")
    id_emp = input("Inser id_emp: ")
    ename = input("Insert employee name: ")
    job = input("insert job: ")
    mgr = input("Inser mgr: ")
    hiredate = input("Insert hiredate: ")
    sal = input("insert sal: ")
    comm = input("Inser comm: ")
    deptno = input("Insert deptno: ")
    new_employee = employee.Employee(id_emp, ename, job,mgr,hiredate,sal,comm,deptno)
    department_gateway.DepartmentGateway.insert_department(new_employee)


menu()