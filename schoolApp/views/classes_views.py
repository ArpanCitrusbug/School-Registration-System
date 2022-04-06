from schoolApp.models import Class
from django.shortcuts import render,redirect
from django.views.generic import *



class TeacherClassCreateView(CreateView):

    model = Class
    # formclass=AddSchoolForm
    template_name ="classform.html"
    success_url = "/teacher_mainbody"
    fields = '__all__'