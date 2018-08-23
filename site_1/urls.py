from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.search, name='index'),
	path('quem_somos/', views.quem_somos, name='quem_somos'),
	path('anuncie/', views.anuncie, name='anuncie'),
	#path('', views.atualizar, name='atualizar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)