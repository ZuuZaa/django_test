from django.shortcuts import render, redirect
from .models import NewsModel
from .forms import NewsForm

# Create your views here.
def home(request):

    news_list = NewsModel.objects.all()
    context = {
        'news_list' : news_list
    }

    return render(request, 'index.html', context)


def news_detail(request, slug):

    news = NewsModel.objects.filter(slug=slug).last()
    if news:
        context = {
            'news' : news
        }
        return render(request, 'news_detail.html', context)
    else:
        return redirect('home')


def news_update(request, id):

    news = NewsModel.objects.filter(id=id).last()
    form = NewsForm(instance=news)
    if news:
        context = {
            'news' : news,
            'form' : form
        }
        print('--------------update')
        return render(request, 'news_update.html', context)
    else:
        print('--------------update')
        return redirect('home')



