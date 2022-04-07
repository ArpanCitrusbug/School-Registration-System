from django.shortcuts import render,redirect
from django.views.generic import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth
from django.db.models import Q
from schoolApp.models import *
from django.core import serializers
from django.http import JsonResponse



class StudentSignUpView(View):
    def get(self, request):
        return render(request, 'student_signup.html')

    def post(self, request):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        phone = request.POST['phone']
        email = request.POST['email']
        password2 = request.POST['password2']
        if len(firstname) != 0 and len(lastname) != 0 and len(username) != 0 and len(password1) != 0 and len(
                email) != 0 and len(password2) != 0 and len(phone) != 0:
            if not Student.objects.filter(username=username).exists():
                if password1 == password2:
                    student = Student.objects.create(first_name=firstname, last_name=lastname, username=username,
                                               password=make_password(password1), email=email, phone=phone)
                    student.save()
                    return redirect('/student_login/')
                else:
                    messages.error(request, "Password Doesn't Match")
            else:
                messages.info(request, "Username is already taken")
        else:
            messages.info(request, "All fields are Required")
        return render(request, 'index.html')



class StudentLogInView(View):
    def get(self, request):
        return render(request, 'student_login.html')
        

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        student = Student.objects.get(username=username)
        id = student.pk
        password_check = check_password(password, student.password)
        # print(password_check)

        auth.login(request, student)
        return redirect(f'/student_mainbody/{id}')
    

class StudentLogout(View):
    def get(self, request):
        auth.logout(request)
        return redirect('StudentLogIn')


class StudentMainBodyView(View):
    def get(self, request,id):
        student = Student.objects.get(id=id)
        
        

        context ={
            "student":student,
        }
        return render(request,'student_mainbody.html',context)


class StudentAccessCodeSearchView(View):
        def get(self, request):
            searched = request.GET.get('searched')
            product_searched = Class.objects.filter(access_code__icontains=searched)
            for i in product_searched:
                student_list = [j.username for j  in i.student_name.all()]
            for i in product_searched:
                teacher_list = [j.username for j  in i.teacher_name.all()]
            print(teacher_list)
            # class_student_list=Student.objects.filter(username__in=student_list)
            
            product_searched_json = serializers.serialize('json', product_searched)
            # class_student_list_json = serializers.serialize('json', class_student_list)
            context={
                "class_student_list_json":student_list,
                "teacher_list_json":teacher_list,
                "product_searched_json":product_searched_json,
            }
            return JsonResponse(context,safe=False)








    # def get(self,request):
    #     searched = request.GET['searched']
    #     classs = Class.objects.filter(Q(access_code__icontains=searched))
    #     return render(request,'student_mainbody.html',{'searched':searched,
    #     'classs':classs})
        