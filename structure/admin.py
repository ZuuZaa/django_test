from django.contrib import admin
from .models import Department, Person

# Register your models here.
@admin.register(Department)
class Departments_Admin(admin.ModelAdmin):
    list_display = ['name','address']


@admin.register(Person)
class Person_Admin(admin.ModelAdmin):
    list_display = ['full_name','role']