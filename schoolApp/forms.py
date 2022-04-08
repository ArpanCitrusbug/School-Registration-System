from django import forms
from django.forms import ModelForm
from .models import School, Student

class AddSchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['school_name','address','school_phone','teacher_id']


class UpdateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','email']