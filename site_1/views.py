from django.shortcuts import render
from django.utils import timezone
from .models import Produto
from .filtrar import ProdutoFilter

#def atualizar(request):
#	ofertas = Produto.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
#	return render(request, 'site_1/ofertas.html', {'ofertas': ofertas})

def quem_somos(request):
	ofertas = Produto.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
	return render(request, 'site_1/quem_somos.html', {'ofertas': ofertas})

def anuncie(request):
	return render(request, 'site_1/anuncie_aqui.html', {})

def search(request):
    oferta_select = Produto.objects.filter(data_publicacao__lte=timezone.now()).order_by('-data_publicacao')
    oferta_select = ProdutoFilter(request.GET, queryset=oferta_select)
    return render(request, 'site_1/index.html', {'oferta_select': oferta_select})
