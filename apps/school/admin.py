from django.contrib import admin

from apps.school.models import Course, Student


admin.site.register(Student)
admin.site.register(Course)
