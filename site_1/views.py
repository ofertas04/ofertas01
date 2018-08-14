from django.shortcuts import render

def listar_ofertas(request):
	return render(request, 'site_1/listar_ofertas.html', {})