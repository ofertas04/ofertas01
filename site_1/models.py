from django.db import models
from django.utils import timezone

#Models do banco de dados

class Produto(models.Model):
	codigo_acesso = models.CharField(max_length=20, primary_key=True)
	descricao = models.CharField(max_length=100)
	link = models.CharField(max_length=200)
	data_publicacao = models.DateTimeField(blank=True, null=True)

	def publicar(self):
		self.data_publicacao = timezone.now()
		self.save()


	def __str__(self):
		return 'Codigo: ' + self.codigo_acesso + '-' + self.descricao