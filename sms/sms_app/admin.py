from django.contrib import admin
from sms_app.models import Student, Teacher, Subject, Department, Assesment, Assignment, Cls

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Assignment)
admin.site.register(Assesment)
admin.site.register(Department)
admin.site.register(Cls)