from django.contrib import admin
from .models import About

# Register your models here.
@admin.register(About)
class About_Admin(admin.ModelAdmin):
    list_display = ['title','description']