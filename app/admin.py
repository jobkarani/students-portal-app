from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Parent)
admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(Results)
admin.site.register(Unit)
admin.site.register(RegisterUnits)