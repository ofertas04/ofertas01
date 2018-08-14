from django.shortcuts import render
from django.utils import timezone
from .models import Produto

def listar_ofertas(request):
	ofertas = Produto.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
	return render(request, 'site_1/listar_ofertas.html', {'ofertas': ofertas})