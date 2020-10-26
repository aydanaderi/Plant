from django.shortcuts import render,get_object_or_404
from difflib import SequenceMatcher
from . import models

def HomeView(request):
    return render(request, 'home.html')

def SearchView(request):
    if 'term' in request.GET :
       db = models.Plant.objects.filter(name__icontains = request.GET.get('term'))
       ls = list()
       for s in db :
            ls.append(s.ls)
            return render(request,'plant.html',{'ls' : ls})
       return render(request, 'plant1.html', {'error': 'یافت نشد'})
    return render(request,'plant1.html')

def ResultView(request,name_id):
    name = get_object_or_404(models.Plant,pk = name_id)
    print(name_id)
    plnt = models.Plant.objects.all()
    for l in models.Plant.objects.all():
        if str(l.name) == str(name):
            return render(request, 'plant.html', {'name': name, 'plnt': plnt})
    return render(request, 'plant1.html', {'error': 'یافت نشد'})

"""def SearchView(request):
    if request.method == "POST":
        name = request.POST['search']
        max = 0.6
        db = ''
        for l in models.Plant.objects.all():
            ratio1 = SequenceMatcher(None, l.name, name).ratio()
            if ratio1 > 0.8 :
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
        return render(request, 'search.html')"""