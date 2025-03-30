from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('Lista/', views.lista, name='lista')
]

#python manage.py runserver