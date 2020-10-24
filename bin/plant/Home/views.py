from django.shortcuts import render,redirect
from django.http import HttpResponse
from difflib import SequenceMatcher
from . import models

def HomeView(request):
    return render(request, 'home.html')

def SearchView(request):
    if request.method == "POST":
        name = request.POST['search']
        list = []
        for l in models.Plant.objects.all():
            ratio1 = SequenceMatcher(None, l.name, name).ratio()
            if ratio1 > 0.6 :
                list.append(l.name)
                print(ratio1)
        if len(list) == 0 :
            return render(request, 'search.html', {'error': 'یافت نشد'})
        else :
            return render(request,'plant.html')
    else:
        return render(request, 'search.html')