from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('listas/', views.listas, name='listas'),
    path('listas/<int:id>', views.lista, name='lista'),
]