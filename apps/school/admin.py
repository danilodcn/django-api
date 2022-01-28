from django.contrib import admin

from apps.school.models import Course, Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "cpf", "rg", "birth_date"]
    list_display_links = ["id", "name"]
    list_per_page = 20
    search_fields = ["id", "name", "cpf"]


class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "code", "level"]
    list_display_links = ["id", "title"]
    list_per_page = 20
    search_fields = ["id", "title", "code", "level"]


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
