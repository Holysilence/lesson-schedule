from django.contrib import admin

from .models import Student

from.models import Location

@admin.register(Student,Location)
class StudentAdmin(admin.ModelAdmin):
    pass
