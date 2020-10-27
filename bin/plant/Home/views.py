from django.shortcuts import render,get_object_or_404
from difflib import SequenceMatcher
from . import models

def HomeView(request):
    return render(request, 'home.html')

def SearchView(request):
    if request.method == "POST":
        name = request.POST['search']
        db = list()
        for l in models.Plant.objects.all():
            ratio = SequenceMatcher(None, l.name, name).ratio()
            if ratio > 0.6 :
                db.append(l.name)
        if db == '' :
            return render(request, 'search.html', {'error': 'یافت نشد'})
        else :
            plnt = models.Plant.objects.all()
            return render(request, 'result.html', {'db' : db,'plnt' : plnt})
    else:
        return render(request, 'search.html')

def ResultView(request,name_id):
    name = get_object_or_404(models.Plant, pk = name_id)
    name = str(name)
    plnt = models.Plant.objects.all()
    return render(request, 'plant.html', {'name': name, 'plnt': plnt})