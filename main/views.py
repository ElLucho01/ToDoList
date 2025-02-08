from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Lista
from django.contrib.auth.models import User
from .forms import CreateNewList

# Create your views here.

def home(request):
    return HttpResponseRedirect("/listas/")

def listas(response):
    if response.user.is_authenticated:
        ls = Lista.objects.filter(user=response.user)
        if response.method == "POST":
            if(response.POST.get("newList")):
                if len(response.POST["name"]) > 2:
                    n = response.POST["name"]
                    user = User.objects.get(id=response.user.id)
                    t = Lista(name=n, user=user)
                    t.save()
                    return HttpResponseRedirect(".") # This is to avoid the form resubmission warning
            elif(response.POST.get("deleteList")):
                for lista in ls:
                    if response.POST.get("c" + str(lista.id)):
                        lista.delete()
    else:
        return HttpResponseRedirect("/login")
    return render(response, 'main/listas.html', {"ls": ls})

def remLista(response, id):
    ls = Lista.objects.get(id=id)
    if response.method == "GET":
        ls.delete()
    return HttpResponseRedirect("/listas/")

def lista(response, id):
    ls = Lista.objects.get(id=id)
    if response.method == "POST":
        ls.item_set.create(text=response.POST["name"], complete=False)
    return render(response, 'main/lista.html', {"ls": ls})

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