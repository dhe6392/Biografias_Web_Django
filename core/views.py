from django.shortcuts import render
from . models import *
from django.shortcuts import get_object_or_404

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



def detalhe(request,id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    context = {
        'pessoa': pessoa
    }
    return render(request, 'core/detalhe.html', context = context)