from django.urls import path
from schoolApp.views.classes_views import *
from schoolApp.views.schools_views import *
from schoolApp.views.students_views import *
from schoolApp.views.teachers_log_views import *
from schoolApp.views.teachers_views import *
# from . import views

urlpatterns = [
#Teacher's URL
    path('', IndexView.as_view(), name="Index"),
    path('teachersignup/',TeacherSignUpView.as_view(), name="TeacherSignUp"),
    path('teacherlogin/',TeacherLogInView.as_view(), name='TeacherLogIn'),
    path('teachermainbody/',TeacherMainBodyView.as_view(), name="TeacherMainBody"),


#Student's URL
    path('studentsignup/',StudentSignUpView.as_view(), name="StudentSignUp"),
    path('student_login/',StudentLogInView.as_view(), name='StudentLogIn'),
    path('student_mainbody/',StudentMainBodyView.as_view(), name="StudentMainBody"),


#
]