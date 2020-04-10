from django.shortcuts import render
from .models import News

# Create your views here.
def home(request):

    news_list = News.objects.all()

    for i in news_list:
        if i.img:
            print(i.img.url) 
        else:
            print('------ else') 

    context = {
        'news_list' : news_list
    }

    return render(request, 'index.html', context)
