from django.shortcuts import render,redirect
from django.views.generic import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from schoolApp.models import Teacher

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class TeacherSignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'teacher_signup.html')

        else:
            return render(request, 'index.html')
    # return redirect('login')

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
            if not Teacher.objects.filter(username=username).exists():
                if password1 == password2:
                    teacher = Teacher.objects.create(first_name=firstname, last_name=lastname, username=username,
                                               password=make_password(password1), email=email, phone=phone)
                    teacher.save()
                    return redirect('MainBody')
                else:
                    messages.error(request, "Password Doesn't Match")
            else:
                messages.info(request, "Username is already taken")
        else:
            messages.info(request, "All fields are Required")
        return render(request, 'index.html')