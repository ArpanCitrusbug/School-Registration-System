from django.urls import path
from school_api.views.teachers_views import *
from school_api.views.student_views import *
from school_api.views.school_views import *
from school_api.views.class_views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView


urlpatterns = [
    # Teacher API
    path('teacher/list/', TeacherAPI.as_view()),
    path('teacher/<int:id>/', TeacherAPI.as_view()),

    #Student API
    path('student/list/', StudentAPI.as_view()),
    path('student/<int:id>/', StudentAPI.as_view()),

    #School API
    path('school/list/', SchoolAPI.as_view()),
    path('school/<int:id>/', SchoolAPI.as_view()),

    #Class API
    path('class/list/', ClasssAPI.as_view()),
    path('class/<int:id>/', ClasssAPI.as_view()),

    #Token Authnetication API
    # path('get-token/simple-token/auth/', obtain_auth_token),

    #JWT Token Authentication API
    path('get-token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh-token/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verify-token/', TokenVerifyView.as_view(), name='token_verify')
]