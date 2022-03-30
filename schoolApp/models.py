from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class Teacher(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    username = models.CharField(max_length=40, blank=True, null=True,default='')
    password = models.CharField(max_length=20)




class Student(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    username = models.CharField(max_length=40, blank=True, null=True,default='')
    password = models.CharField(max_length=20)




class Class(models.Model):
    standard = models.IntegerField(max_length=12, blank= True)
    division = models.CharField(blank=True)
    access_code = models.CharField()
    student = models.ManyToManyField(Student,null=False, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher, null=False, on_delete=models.CASCADE)



class School(models.Model):
    school_name = models.CharField(max_length=40, blank=True)
    address = models.CharField( blank=True)
    school_phone = models.CharField(max_length=15, blank=True)
    teacher = models.ManyToManyField( Teacher, null=False, on_delete=models.CASCADE)
    class_field = models.ManyToManyField(Class, on_delete=models.CASCADE)
