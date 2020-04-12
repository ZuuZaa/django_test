from django.urls import path
from .views import home, news_detail, news_update

urlpatterns = [
    path('', home, name='home'),
    path('news/<str:slug>/', news_detail, name='news_detail'),
    path('news/<int:id>/update/', news_update, name='news_update'),
]