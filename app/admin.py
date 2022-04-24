from django.conf import settings
# from .models import User
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import User
# Register your models here.

admin.site.register(User)
admin.site.register(Parent)
admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(Results)
admin.site.register(Unit)
admin.site.register(RegisterUnits)