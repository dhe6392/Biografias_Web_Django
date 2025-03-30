from django.shortcuts import render
from . models import *

def index (request):
    return render(request, 'core/index.html')

def lista(request):
    pesquisa = request.GET.get('pesquisa')

    if pesquisa:
        pessoas = Pessoa.objects.filter(biografia__contains=pesquisa)
    else:
        pessoas = Pessoa.objects.all()
        
    context = {
        'pessoas': pessoas
    }
    return render(request, 'core/lista.html', context = context)