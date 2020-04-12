from django.contrib import admin
from .models import Application

# Register your models here.
@admin.register(Application)
class Application_Admin(admin.ModelAdmin):
    list_display = ['first_name','last_name','request_type','content']
    readonly_fields = ['first_name','last_name','request_type','department','subject','email','content']