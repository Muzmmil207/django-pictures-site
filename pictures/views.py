from django.shortcuts import redirect, render
import requests
import json
from django.core.paginator import Paginator
from django.db.models import Q
import random
# Create your views here.
quary = ['', 'wallpaper', 'hd', 'Love', 'Ocean',
         'Flower', 'Art', 'Fashion', 'Pet', 'Colorful']


def MainPage(request):
    # ---------------------------------
    arr = []
    url2 = '''https://pixabay.com/api/?key=28649987-1dbe522815c3603c4504c8384&image_type=photo&q=HD&per_page=200'''
    API2 = requests.get(url2)
    data2 = API2.text
    json_obj2 = json.loads(data2)
    for i in json_obj2['hits']:
        arr.append(i.get('largeImageURL'))
    # ----------------------------

    json_objs = json_obj2['hits']

    for x in quary:
        url = '''https://pixabay.com/api/?key=28649987-1dbe522815c3603c4504c8384&image_type=photo&q=''' + \
            x+'''&per_page=200'''
        API = requests.get(url)
        data = API.text
        json_obj = json.loads(data)
        json_objs += json_obj['hits']

    random.shuffle(json_objs)
    p = Paginator(json_objs, 50)
    page = request.GET.get('page')
    pictures = p.get_page(page)
    return render(request, 'pictures/main-page.html', {'pages': pictures, 'head': arr})


def PhotoDetails(request, pk, tags):
    #q = request.GET.get('x')
    url = '''https://pixabay.com/api/?key=28649987-1dbe522815c3603c4504c8384&image_type=photo&q=''' + \
        tags + '''&per_page=200'''
    API = requests.get(url)
    data = API.text
    json_obj = json.loads(data)
    pic = None
    for i in json_obj['hits']:
        if i['id'] == int(pk):
            pic = i

    return render(request, 'pictures/photo-detail.html', {'jo': pic, 'josn': json_obj['hits'][:8]})


def categore(request):
    e = "muzmmila141@gmail.com"
    return render(request, 'pictures/categore.html', {'e': e})


def SearchPage(request):
    q = request.GET.get('q')
    url = '''https://pixabay.com/api/?key=28649987-1dbe522815c3603c4504c8384&image_type=photo&q=''' + \
        str(q) + '''&per_page=200'''

    API = requests.get(url)
    data = API.text
    json_obj = json.loads(data)
    p = Paginator(json_obj['hits'], 15)
    page = request.GET.get('page')
    pictures = p.get_page(page)
    return render(request, 'pictures/search.html', {'pages': pictures, 'q': q})


def Contact(request, email):
    return redirect(email)


def about(request):
    page = 'about'
    return render(request, 'pictures/about.html', {'page': page})


def UseAgreement(request):
    page = 'UseAgreement'
    return render(request, 'pictures/about.html', {'page': page})


def PrivacyPolicy(request):
    return render(request, 'pictures/PrivacyPolicy.html')


def about(request):
    return render(request, 'pictures/about.html')
