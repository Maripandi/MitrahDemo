"""
Definition of models.
"""

from django.db import models
# Create your models here.


class Departments(models.Model):
    
    name=models.CharField(max_length=40)
    id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Designations(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    department=models.ForeignKey(Departments, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name

class Employees(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    salary=models.FloatField()
    department=models.ForeignKey(Departments, on_delete = models.SET_NULL, null=True, blank=True)
    designations=models.ForeignKey(Designations, on_delete = models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name