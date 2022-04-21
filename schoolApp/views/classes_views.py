from schoolApp.models import *
from django.shortcuts import render,redirect
from django.views.generic import *
from schoolApp.forms import AddClassForm


class TeacherClassCreateView(View):
    def get(self,request):
        if request.user.is_authenticated:
            form = AddClassForm
            return render(request, 'classform.html',{'form':form})
        else:
            return render(request,'teacherlogin.html')

    def post(self, request):
        standard = request.POST['standard']
        division = request.POST['division']
        access_code = request.POST['access_code']
        classs = Classs.objects.create(standard=standard, division=division, access_code=access_code)
        classs.save()
        classs.teacher_name.add(request.user)
        school = request.user.teacher_info.first()
        school.class_field.add(classs)
        return redirect('TeacherMainBody')    


class TeacherClassUpdateView(UpdateView):
    model=Classs
    template_name ="classform.html"
    success_url = "/teacher_mainbody"
    fields = '__all__'