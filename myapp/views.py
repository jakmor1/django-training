import random
import urllib.request

from django.shortcuts import render


def home_view(request):
    number = random.randint(1, 100)
    some_list = [
      random.randint(1, 100),
      random.randint(1, 100),
      random.randint(1, 100),
    ]
    some_dict = {
      'A': 1,
      'B': 2,
      'C': 3
    }
    context = {
      'mynumber': number,
      'bool_item': True,
      'some_list': some_list,
      'some_dict': some_dict,
    }
    return render(request, 'myapp/index.html', context)


def about_view(request):
    mytech = [
        {
          'name': 'HTML',
          'url': 'https://www.w3schools.com/html/',
          'level': 'beginner'
        },
        {
          'name': 'CSS',
          'url': 'https://www.w3schools.com/css/',
          'level': 'beginner'
        },
        {
          'name': 'Bootstrap',
          'url': 'https://getbootstrap.com',
          'level': 'beginner'
        },
        {
          'name': 'Python',
          'url': 'https://www.python.org',
          'level': 'intermediate'
        },
        {
          'name': 'Django',
          'url': 'https://www.djangoproject.com',
          'level': 'beginner'      
        },    
    ]
    context = {
        'lucky_number': random.randint(1, 10),
        'unlucky_number': random.randint(1, 10),
        'mytech': mytech, 
    }
    return render(request, 'myapp/about.html', context)


def contact_view(request):
    return render(request, 'myapp/contact.html')


def genbank_view(request):
    URL = 'ftp://ftp.ncbi.nlm.nih.gov/genbank/README.genbank'
    response = urllib.request.urlopen(URL)
    data = response.read() 
    text = data.decode('utf-8')
    release = text.split('\n')[2]
    date = text.split('\n')[9]
    context = {
      'gb_release' : release.strip().split()[4],
      'gb_date' : " ".join(date.strip().split()[1:5])
    }
    return render(request, 'myapp/genbank.html', context)