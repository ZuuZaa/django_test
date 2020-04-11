from django.contrib import admin
from .models import News

# Register your models here.
@admin.register(News)
class News_Admin(admin.ModelAdmin):

    list_display = ['title','content','published','get_image']
    readonly_fields = ['slug','published']