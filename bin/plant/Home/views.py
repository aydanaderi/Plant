from django.shortcuts import render,redirect
from . import models

def HomeView(request):
    return render(request, 'home.html')

def SearchView(request):
    if request.method == "POST":
        name = request.POST['search']
        for l in models.Plant.objects.all():
            if l.name == name :
                return redirect('/home')
            if l.English_name == name :
                return redirect('/home')
        return render(request, 'search.html', {'error': 'یافت نشد'})
    else:
        return render(request, 'search.html')