from django.db import models

# Create your models here.


from app.models import *


class DEPT(models.Model):
    DEPT_NO = models.IntegerField(primary_key=True)     
    Dname= models.CharField(max_length=100, unique=True)
    LOC = models.CharField(max_length=100, unique=True)


class EMP(models.Model):
    EMPNO = models.IntegerField(unique=True)
    Ename = models.CharField(max_length=100)
    JOB = models.CharField(max_length=100)
    MGR = models.IntegerField()
    HIREDATE  = models.DateField()
    SAL = models.FloatField()
    Comm = models.IntegerField(null= True)
    DEPT_NO = models.ForeignKey(DEPT, on_delete= models.CASCADE)
    
class SALGRADE(models.Model):
    salg = models.CharField(max_length=10)
    
class Bonus(models.Model):
    Bons = models.IntegerField()
    
    