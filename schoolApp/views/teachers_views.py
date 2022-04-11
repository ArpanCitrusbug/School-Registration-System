from django.shortcuts import render,redirect
from django.views.generic import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth
from schoolApp.models import Teacher, School,Class

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request,'index.html')
    # def get(self, request):
    #     if request.user.is_authenticated:
    #         school = School.objects.all()
    #         context = {
    #             "schools":school,
    #         }
    #         return render(request, 'teacher_mainbody.html', context)
    #     else:
    #         return redirect("TeacherLogIn")



class TeacherSignUpView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('TeacherMainBody')
        else:
            return render(request,"teacher_signup.html")
        # return render(request, 'teacher_signup.html')


            # return render(request, 'index.html')
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
                                                email=email, phone=phone)
                    teacher.set_password(password1)
                    teacher.save()
                    return redirect('/teacherlogin/')
                else:
                    messages.error(request, "Password Doesn't Match")
            else:
                messages.info(request, "Username is already taken")
        else:
            messages.info(request, "All fields are Required")
        return render(request, 'index.html')


class TeacherLogInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'teacher_mainbody.html')
        else:
            return render(request,"teacherlogin.html")
        
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        teacher = Teacher.objects.get(username=username)
        print(teacher.password)
        password_check = check_password(password, teacher.password)
        if password_check:
            auth.login(request, teacher)
            return redirect('TeacherMainBody')
        return render(request, 'teacher_mainbody.html')



class TeacherMainBodyView(View):
    def get(self, request):
        if request.user.is_authenticated:
            school = School.objects.all()
            context = {
                "schools":school,
            }
            return render(request, 'teacher_mainbody.html', context)
        else:
            return redirect("TeacherLogIn")


class TeacherSchoolDetailedView(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            school = School.objects.get(id=id)
            class_name = Class.objects.filter(id = id)
            context = {
                "school":school,
                "class":class_name,
            }
            return render(request, 'teacher_school_detail.html',context)
        else:
            return redirect("TeacherLogIn")


class TeacherSchoolCreateView(CreateView):
    # def get(self, request):
    #     form = AddSchoolForm
    #     return render(request, 'schoolform.html',{'form':form})
    model = School
    # formclass=AddSchoolForm
    template_name ="schoolform.html"
    success_url = "/teacher_mainbody"
    fields = '__all__'

    # def post(self, request):
    #     school_name = request.POST['school_name']
    #     address = request.POST['address']
    #     school_phone = request.POST['school_phone']
    #     teacher_id = request.POST['teacher_id']
    #     # class_field = request.POST['class_field']
        
    #     teacher_id=Teacher.objects.filter(pk = teacher_id)
    #     post = School.objects.create(school_name=school_name, address=address, school_phone=school_phone,
    #                                    teacher_id=teacher_id.set(), admin_id = request.user)
    #     post.save()
    #     return redirect('TeacherMainBody')


class TeacherLogout(View):
    def get(self, request):
        auth.logout(request)
        return render(request,'teacherlogin.html')