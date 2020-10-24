from django.shortcuts import render,redirect
from django.http import HttpResponse
from difflib import SequenceMatcher
from django.views import generic
from . import models

def HomeView(request):
    return render(request, 'home.html')

def SearchView(request):
    if request.method == "POST":
        name = request.POST['search']
        list = []
        max = 0.6
        db = ''
        for l in models.Plant.objects.all():
            ratio1 = SequenceMatcher(None, l.name, name).ratio()
            if ratio1 > 0.6 :
                if ratio1 == 1:
                    db = l.name
                    break
                if ratio1 > max:
                    max = ratio1
                    db = l.name
        if db == '' :
            return render(request, 'search.html', {'error': 'یافت نشد'})
        else :
            plnt = models.Plant.objects.all()
            return render(request, 'plant.html', {'db' : db,'plnt' : plnt})
    else:
        return render(request, 'search.html')
