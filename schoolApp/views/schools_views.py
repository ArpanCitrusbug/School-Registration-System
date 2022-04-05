from django.shortcuts import render,redirect
from django.views.generic import *
from schoolApp.models import School
from schoolApp.forms import AddSchoolForm

class CreateSchoolView(View):
    def get(self,request):
        form = AddSchoolForm
        return render(request, 'schoolform.html',{'form':form})

    def post(self, request):
        school_name = request.POST['school_name']
        address = request.POST['address']
        school_phone = request.POST['school_phone']
        school = School.objects.create(school_name=school_name, address=address, school_phone=school_phone,
                                        user = request.teacher)
        school.save()
        return redirect('TeacherMainBody')