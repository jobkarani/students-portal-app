
  
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile, name='profile'),
    path('createstudent/', views.createStudent, name='createStudent'),
    path('createUnit/', views.createUnit, name='createUnit'),
    path('createSem/', views.createSem, name='createSem'),
    path('createResults/', views.createResults, name='createResults'),
    path('units/', views.viewUnits, name='viewUnits'),
    path('semesters/', views.viewSems, name='viewSems'),
    path('results/', views.viewResults, name='viewResults'),
    # path('removeSem/<int:semester_name>/', views.removeSem, name='removeSem'),
    path('result-chart/', views.bar_chart, name='bar_chart'),
    path('bar-chart/', views.bar_chart, name='bar_chart'),
]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       