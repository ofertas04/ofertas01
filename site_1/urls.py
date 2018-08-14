from django.urls import path
from . import views

urlpatterns = [
	path('', views.listar_ofertas, name='listar_ofertas'),
]