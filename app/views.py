from django.shortcuts import render

from django.http import HttpResponse

from app.models import *

def check(request):
    return HttpResponse("hello")

# Create your views here.


def insert_dept(request):
    print('we have existing dept data')
    Existing_dept = DEPT.objects.all()
    for dept in Existing_dept:
        print(dept.DEPTNO, dept.DNAME, dept.LOC)
    print('Inserting new dept data')
    DNO = input("Enter dept no: ")
    DN = input("Enter dept name: ")
    DLOC = input("Enter dept location: ")
    Departmenttableobject = DEPT.objects.get_or_create(DEPTNO= DNO, DNAME=DN, LOC=DLOC)
    if Departmenttableobject[1]:
        return HttpResponse("Department data inserted successfully")
    else:
        return HttpResponse("Department data already exists")
def insert_emp(request):
    print('Web have existing emp data')
    Existing_emp = EMP.objects.all()
    for emp in Existing_emp:
        print(emp.EMPNO, emp.ENAME, emp.JOB, emp.MGR, emp.HIREDATE, emp.SAL, emp.COMM, emp.DEPTNO)
    print('Inserting new emp data')
    ENO = input("Enter emp no: ")
    EN = input("Enter emp name: ")
    EJOB = input("Enter emp job: ")
    EMGR = input("Enter emp mgr: ")
    if EMGR:
        EMGR = int(EMGR)
    else:
        EMGR = None
    EHIREDATE = input("Enter emp hiredate (YYYY-MM-DD: ")
    ESAL = float(input('Enter emp sal: '))
    ECOMM = input("Enter emp comm: ")
    if ECOMM:
        ECOMM = int(ECOMM)
    else:
        ECOMM = None
    EDEPTNO = int(input("Enter emp deptno: "))
    LISTOFDEPT = DEPT.objects.filter(DEPTNO = EDEPTNO)
    if LISTOFDEPT:
        DEPTTABLEOBJECT = LISTOFDEPT[0]
        Emptableobject = EMP.objects.get_or_create(EMPNO= ENO, ENAME=EN, JOB=EJOB, MGR=EMGR, HIREDATE=EHIREDATE, SAL=ESAL, COMM=ECOMM, DEPTNO=DEPTTABLEOBJECT)
        if Emptableobject[1]:
            return HttpResponse("Employee data inserted successfully")
        else:
            return HttpResponse("Employee data already exists")
    else:
        return HttpResponse("Deptno does not exist. Cannot insert employee data")