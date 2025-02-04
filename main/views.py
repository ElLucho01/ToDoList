from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Lista
from .forms import CreateNewList

# Create your views here.

def home(request):
    return render(request, 'home.html')

def listas(response):
    ls = Lista.objects.all()
    if response.method == "POST":
        if len(response.POST["name"]) > 2:
            t = Lista(name=response.POST["name"])
            t.save()
        return HttpResponseRedirect(".")
    else:
        form = CreateNewList()
    return render(response, 'listas.html', {"form": form, "ls": ls})

def lista(response, id):
    ls = Lista.objects.get(id=id)
    if response.method == "POST":
        ls.item_set.create(text=response.POST["name"], complete=False)
    return render(response, 'lista.html', {"ls": ls})