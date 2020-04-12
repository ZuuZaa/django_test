from django.contrib import admin
from .models import NewsModel

# Register your models here.
@admin.register(NewsModel)
class News_Admin(admin.ModelAdmin):

    list_display = ['title','content']
    readonly_fields = ['slug','published']