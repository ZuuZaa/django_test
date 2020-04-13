from django.shortcuts import render, redirect
from .models import NewsModel
from .forms import NewsForm
from structure.models import Department, Person
from about.models import About 

# Create your views here.
def home(request):

    news_list = NewsModel.objects.all()
    department_list = Department.objects.all()
    about = list(About.objects.all())[-1]
    person_list = Person.objects.all()
    context = {
        'about' : about,
        'news_list' : news_list,
        'department_list' : department_list,
        'person_list' : person_list,
    }

    if request.method == 'POST':

        request_type = request.POST.get('type')
        department = request.POST.get('structure')
        subject = request.POST.get('subject')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('fsurname')
        email = request.POST.get('email')
        prefix = str(request.POST.get('prefix'))
        number = str(request.POST.get('fnumber'))
        phone_number = '+994' + prefix + number
        content = request.POST.get('fmsj')
        print('--------')
        print(request.POST)
        print(phone_number)
        print(email)
    
    else:
        pass

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



