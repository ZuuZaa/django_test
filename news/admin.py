from django.contrib import admin
from .models import News

# Register your models here.
@admin.register(News)
class News_Admin(admin.ModelAdmin):

    list_display = ['title','publised','get_image']
    readonly_fields = ['get_image']