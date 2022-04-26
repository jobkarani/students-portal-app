from django.urls import URLPattern, URLResolver,path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views as app_views
from http import server
from unicodedata import name
from django import urls


urlpatterns = [
    path('', views.index, name='index'),
    path('register/options/', views.options, name='options'),
    path('aboutus/', views.aboutUs, name='aboutUs'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/student/', views.student_signup, name='student_signup'),
    path('signup/parent/', views.parent_signup, name='parent_signup'),
    path('dashboard/', app_views.dashboard, name='dashboard'),
    path('createstudent/', views.createStudent, name='createStudent'),
    path('viewStudent/', views.viewStudents, name='viewStudents'),
    path('createUnit/', views.createUnit, name='createUnit'),
    path('regUnit/', views.registerUnits, name='regUnit'),
    path('createterm/', views.createSem, name='createSem'),
    path('createResults/', views.createResults, name='createResults'),
    path('units/', views.viewUnits, name='viewUnits'),
    path('terms/', views.viewSems, name='viewSems'),
    path('results/', views.viewResults, name='viewResults'),
    path('removeSem/<slug>/', views.removeSem, name='removeSem'),
    path('removeUnit/<slug>/', views.removeUnit, name='removeUnit'),
    path('result-chart/', views.bar_chart, name='bar_chart'),
    path('bar-chart/', views.bar_chart, name='bar_chart'),
    path('pdf/', views.GeneratePdf.as_view(),name='GeneratePdf'),
]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       