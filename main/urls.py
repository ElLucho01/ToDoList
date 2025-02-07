from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('home', views.home, name='home'), 
    path('listas/', views.listas, name='listas'),
    path('listas/<int:id>', views.lista, name='lista'),
    path('listas/rmLista/<int:id>', views.remLista, name='rmLista'),
    path('listas/<int:id>/rmItem/<int:item>', views.rmItem, name='rmItem'),
    path('listas/<int:id>/togItem/<int:item>', views.togItem, name='togItem'),
]