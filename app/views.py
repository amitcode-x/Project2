from django.shortcuts import render

from django.db.models import *

from django.db.models import Q

from django.http import HttpResponse

from app.models import *

from django.db.models import Prefetch

def Homepage(request):
    return render(request,'Homepage.HTML')

# Create your views here.

# Insert data into DEPT table

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

# Display data from DEPT table  
def Display_dept(request):
    LISTOFDEPT = DEPT.objects.all()
    data ={"Depts": LISTOFDEPT}
    return render(request, "Display_Dept.HTML", data)

# Insert data into EMP table
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

# Display data from EMP table

def Display_emp(request):
    LISTOFEMP = EMP.objects.all()
    # LISTOFEMP= EMP.objects.filter(ENAME = 'SMITH')
    # LISTOFEMP = EMP.objects.filter(MGR__gt = 7901)
    
    LISTOFEMP = EMP.objects.filter(SAL__gt = 600)
    
  
    
    # LISTOFEMP = EMP.objects.order_by('ENAME')
    
    # LISTOFEMP = EMP.objects.filter(Q(SAL__gt = 1200) & Q(DEPTNO = 20))
    
    # LISTOFEMP = EMP.objects.filter(SAL__lte = 1200 , DEPTNO =20)
    
    # LISTOFEMP = EMP.objects.filter(Q(SAL__gt = 1200) | Q(DEPTNO = 20))
    
    
  
    
   
    
    
    
    
    data = {"Emps": LISTOFEMP}
    return render(request, "Display_Emp.HTML", data)
def DisplayEMPTODEPTJoin(request):
    Quesrysetlistempdeptobject = EMP.objects.select_related('DEPTNO')
    
    
    
    # Quesrysetlistempdeptobject = EMP.objects.select_related('DEPTNO').filter(DEPTNO__LOC='DALLAS')
    
    d = {'Quesrysetlistempdeptobject': Quesrysetlistempdeptobject}
    
    return render(request, 'DisplayEMPTODEPTjoin.HTML',d)

def DisplayEmpToMgrJoin(request):
    
    Quesrysetlistempmgrobject = EMP.objects.select_related('MGR').all()
    
    
    
    
    
    d = {'Quesrysetlistempmgrobject':  Quesrysetlistempmgrobject}
    return render(request, 'DisplayEmpToMgr.HTML', d)

def DisplayEmpDeptMgrJoin(request):
    QSEDMO = EMP.objects.select_related('DEPTNO','MGR')
    
    d = { 'QSEDMO':QSEDMO }
    return render(request,'DisplayEmpDeptMgrJoin.html',d)



def DisplayDEPTEMPbyPrefetch(request):
    
    Querysetoflistofdeptempobject = DEPT.objects.prefetch_related('emp_set').all()
    
    Querysetoflistofdeptempobject = DEPT.objects.prefetch_related('emp_set').filter(DNAME__in = ('ACCOUNTING', 'RESEARCH'))
    
    Querysetoflistofdeptempobject = DEPT.objects.prefetch_related( Prefetch ('emp_set', queryset= EMP.objects.filter(SAL__gt = 1000)))
    
    
    # ye hai niche aggregates functions ka example
    
    
    # davg = EMP.objects.filter(DEPTNO =10).aggregate(Avg('SAL'))
    # print(davg)
    # a = davg['SAL__avg']
    
    # av = EMP.objects.filter()
    # print(av)
    
    
    # aue ye bhi ahi but dusre tarik se 
    
      # # 30
    
    # mxs = EMP.objects.aggregate(Max('SAL'))
    # print(mxs)
    
    
    d = {'Querysetoflistofdeptempobject' : Querysetoflistofdeptempobject}
    return render(request, 'DisplayDEPTEMPbyPrefetch.html', d)