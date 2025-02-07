from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Lista
from .forms import CreateNewList

# Create your views here.

def home(request):
    return HttpResponseRedirect("/listas/")

def listas(response):
    ls = Lista.objects.all()
    if response.method == "POST":
        if(response.POST.get("newList")):
            if len(response.POST["name"]) > 2:
                t = Lista(name=response.POST["name"])
                t.save()
            return HttpResponseRedirect(".") # This is to avoid the form resubmission warning
        elif(response.POST.get("deleteList")):
            for lista in ls:
                if response.POST.get("c" + str(lista.id)):
                    lista.delete()
    else:
        form = CreateNewList()
    return render(response, 'listas.html', {"form": form, "ls": ls})

def remLista(response, id):
    ls = Lista.objects.get(id=id)
    if response.method == "GET":
        ls.delete()
    return HttpResponseRedirect("/listas/")

def lista(response, id):
    ls = Lista.objects.get(id=id)
    if response.method == "POST":
        ls.item_set.create(text=response.POST["name"], complete=False)
    return render(response, 'lista.html', {"ls": ls})

def rmItem(response, id, item):
    ls = Lista.objects.get(id=id)
    if response.method == "GET":
        ls.item_set.get(id=item).delete()
    return HttpResponseRedirect("/listas/" + str(id))

def togItem(response, id, item):
    ls = Lista.objects.get(id=id)
    if response.method == "GET":
        i = ls.item_set.get(id=item)
        if(i.complete == False):
            i.complete = True
        else:
            i.complete = False
        i.save()
    return HttpResponseRedirect("/listas/" + str(id))