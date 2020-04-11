from django.shortcuts import render, redirect
from .models import News

# Create your views here.
def home(request):

    news_list = News.objects.all()
    context = {
        'news_list' : news_list
    }

    return render(request, 'index.html', context)


def news_detail(request, slug):

    news = News.objects.filter(slug=slug).last()
    if news:
        context = {
            'news' : news
        }
        return render(request, 'news_detail.html', context)
    else:
        return redirect('home')


def news_update(request, id):

    news = News.objects.filter(id=id).last()
    if news:
        context = {
            'news' : news
        }
        print('--------------update')
        return render(request, 'news_update.html', context)
    else:
        print('--------------update')
        return redirect('home')



