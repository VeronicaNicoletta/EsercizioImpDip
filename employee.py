class Employee:

    def __init__(self,id_emp,ename:str,job:str,mgr:int,hiredate:str,sal:float,comm:int,deptno:int):
        self.id=id_emp
        self.ename=ename
        self.job=job
        self.mgr=mgr
        self.hiredate=hiredate
        self.sal=sal
        self.comm=comm
        self.deptno=deptno

    @staticmethod
    def empty_id(id:int):
        emp=Employee(id,None,None,None,None,None,None,None)
        return emp