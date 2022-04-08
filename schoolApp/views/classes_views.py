from schoolApp.models import Class,Student
from django.shortcuts import render,redirect
from django.views.generic import *


class TeacherClassCreateView(CreateView):

    model = Class
    # formclass=AddSchoolForm
    template_name ="classform.html"
    success_url = "/teacher_mainbody"
    fields = '__all__'


class TeacherClassUpdateView(UpdateView):
    model=Class
    template_name ="classform.html"
    success_url = "/teacher_mainbody"
    fields = '__all__'

class TeacherStudentUpdateView(UpdateView):
    model=Student
    template_name="update_student.html"
    success_url="/teacher_mainbody"
    fields = '__all__'