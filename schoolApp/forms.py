from django import forms
from django.forms import ModelForm
from .models import School

class AddSchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['school_name','address','school_phone','teacher_id']