from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
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

def Search(request):
    if request.method == "POST":
        name = request.POST['search']
        plnt = models.Plant.objects.all()
        for l in models.Plant.objects.all():
            if str(l.name) == str(name) :
                return render(request, 'plant.html', {'name': name , 'plnt' : plnt})
        return render(request, 'plant1.html', {'error': 'یافت نشد'})
    if 'term' in request.GET :
        db = models.Plant.objects.filter(name__icontains = request.GET.get('term'))
        name = list()
        for s in db :
            name.append(s.name)
            return render(request,'plant1.html',{'name' : name})
    return render(request,'plant1.html')
