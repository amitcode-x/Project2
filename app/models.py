from django.db import models


# Create your models here.




# DEPT Model

class DEPT(models.Model):
    DEPTNO = models.IntegerField(primary_key=True)     
    DNAME= models.CharField(max_length=100, unique=True)
    LOC = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.DEPTNO}"

# EMP Model
class EMP(models.Model):
    EMPNO = models.IntegerField(unique=True)
    ENAME = models.CharField(max_length=100)
    JOB = models.CharField(max_length=100)
    MGR = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        
        on_delete=models.SET_NULL
    )
    HIREDATE  = models.DateField()
    SAL = models.FloatField()
    COMM= models.IntegerField(null= True)
    DEPTNO = models.ForeignKey(DEPT, on_delete= models.CASCADE)
    
    def __str__(self):
        return str(self.EMPNO)

    

    
class SALGRADE(models.Model):
    salg = models.CharField(max_length=10)
    
class Bonus(models.Model):
    Bons = models.IntegerField()
    
    