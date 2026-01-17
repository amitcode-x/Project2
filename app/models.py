from django.db import models

# Create your models here.


from app.models import *


class DEPT(models.Model):
    DEPTNO = models.IntegerField(primary_key=True)     
    DNAME= models.CharField(max_length=100, unique=True)
    LOC = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.DNAME


class EMP(models.Model):
    EMPNO = models.IntegerField(unique=True)
    ENAME = models.CharField(max_length=100)
    JOB = models.CharField(max_length=100)
    MGR = models.IntegerField( null= True)
    HIREDATE  = models.DateField()
    SAL = models.FloatField()
    COMM= models.IntegerField(null= True)
    DEPTNO = models.ForeignKey(DEPT, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.ENAME
    
class SALGRADE(models.Model):
    salg = models.CharField(max_length=10)
    
class Bonus(models.Model):
    Bons = models.IntegerField()
    
    