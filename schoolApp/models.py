from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
# Create your models here.

class TeacherManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have a valid email address.")

        if not kwargs.get("username"):
            raise ValueError("Users must have a valid username.")

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get("username")
        )

        # account.set_username(username)
        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_superuser = True
        account.is_staff = True
        account.save()

        return account



class Teacher(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(null=True, blank=True, unique=True)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=40, blank=True, null=True,default='')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = TeacherManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    @property
    def is_authenticated(self):
        return True



class Student(AbstractBaseUser):
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    username = models.CharField(max_length=40, blank=True, null=True,default='')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Class(models.Model):
    standard = models.IntegerField(blank= True)
    division = models.CharField(max_length=10)
    access_code = models.CharField(max_length=10, unique=True)
    student_name = models.ManyToManyField(Student)
    teacher_name = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.access_code


class School(models.Model):
    school_name = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=100)
    school_phone = models.CharField(max_length=15, blank=True)
    teacher_id = models.ManyToManyField(Teacher,related_name='teacher_info')
    admin_id = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="admin_info")
    class_field = models.ManyToManyField(Class, null=True)

    def __str__(self):
        return self.school_name







# class TeachersLog(models.Model):
#     school = models.ForeignKey(School, on_delete=models.CASCADE)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)

    