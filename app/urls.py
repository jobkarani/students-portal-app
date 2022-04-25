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
    path('student/profile/', views.profileStudent, name='profileStudent'),
    path('student/profile/<int:id>',
         views.profileStudent, name='profileStudent'),
    path('update_student_profile/', views.update_student_profile,
         name='update_student_profile'),
    path('parent/profile/', views.parentProfile, name='parentProfile'),
    path('update_parent_profile/',
         views.update_parent_profile, name='update_parent_profile'),
    path('signup/student/', views.student_signup, name='student_signup'),
    path('signup/parent/', views.parent_signup, name='parent_signup'),
    path('parent/home/', views.parent_home, name='parent_home'),
    path('student/home/', views.student_home, name='student_home'),
    
    path('dashboard/', app_views.dashboard, name='dashboard'),
    path('lecturer_dashboard/', app_views.lecturerDash, name='lecturerDash'),
    path('search_jobseekers/', views.search_student, name='search_student'),

    path('createstudent/', views.createStudent, name='createStudent'),
    path('viewStudent/', views.viewStudents, name='viewStudents'),
    path('createUnit/', views.createUnit, name='createUnit'),
    path('regUnit/', views.registerUnits, name='regUnit'),
    path('createSem/', views.createSem, name='createSem'),
    path('createResults/', views.createResults, name='createResults'),
    path('units/', views.viewUnits, name='viewUnits'),
    path('semesters/', views.viewSems, name='viewSems'),
    path('results/', views.viewResults, name='viewResults'),
#     path('viewPdfResults/', views.viewPdfResults, name='viewPdfResults'),
    path('removeSem/<slug>/', views.removeSem, name='removeSem'),
    path('removeUnit/<slug>/', views.removeUnit, name='removeUnit'),
    path('result-chart/', views.bar_chart, name='bar_chart'),
    path('bar-chart/', views.bar_chart, name='bar_chart'),
    path('pdf/', views.GeneratePdf.as_view(),name='GeneratePdf'),
]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       