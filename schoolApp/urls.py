from django.urls import path
from schoolApp.views.classes_views import *
from schoolApp.views.schools_views import *
from schoolApp.views.students_views import *
from schoolApp.views.teachers_log_views import *
from schoolApp.views.teachers_views import *
# from . import views

urlpatterns = [
    path('', IndexView.as_view(), name="Index"),
]