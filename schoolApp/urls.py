from django.urls import path
from schoolApp.views.classes_views import *
from schoolApp.views.schools_views import *
from schoolApp.views.students_views import *
from schoolApp.views.teachers_log_views import *
from schoolApp.views.teachers_views import *


urlpatterns = [
#Teacher's URL
    path('', IndexView.as_view(), name="Index"),
    path('teachersignup/',TeacherSignUpView.as_view(), name="TeacherSignUp"),
    path('teacherlogin/',TeacherLogInView.as_view(), name='TeacherLogIn'),
    path('teacher_mainbody/',TeacherMainBodyView.as_view(), name="TeacherMainBody"),
    path('teacher_school_detail/<int:id>',TeacherSchoolDetailedView.as_view(), name="TeacherDetailed"),
    path('teacher_logout/', TeacherLogout.as_view(), name="TeacherLogout"),


#Student's URL
    path('studentsignup/',StudentSignUpView.as_view(), name="StudentSignUp"),
    path('student_login/',StudentLogInView.as_view(), name='StudentLogIn'),
    path('student_mainbody/<int:id>',StudentMainBodyView.as_view(), name="StudentMainBody"),
    path('student_logout/', StudentLogout.as_view(), name="StudentLogout"),


#School's URL
    path('school_create/',TeacherSchoolCreateView.as_view(),name='TeacherSchoolCreate'),


#Class' URL
    path('class_create/',TeacherClassCreateView.as_view(),name='TeacherClassCreate'),
]





#student mainbody ajax request
#change access id of student