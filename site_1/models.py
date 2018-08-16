from django.db import models
from django.utils import timezone

#Models do banco de dados de cada produto

class Produto(models.Model):
	codigo_acesso = models.CharField(max_length=20, primary_key=True)
	img = models.ImageField(null=True, blank= False, upload_to='media/%Y/%m/%d')
	descricao = models.CharField(max_length=100)
	link = models.CharField(max_length=200)
	data_publicacao = models.DateTimeField(blank=True, null=False)

	def publicar(self):
		self.data_publicacao = timezone.now()
		self.save()


	def __str__(self):
		return 'Codigo: ' + self.codigo_acesso + '-' + self.descricao

# Model para emails
#class Email(models.Model):
#	nome = models.CharField(max_length=50)
#	email = models.CharField(max_length=200)
#	assunto = models.CharField(max_length=100)
#	telefone = models.IntegerFiled(max_length=11)
#	mensagem = models.TextField()
#	data_envio = models.DateTimeField(blank=False, null=False)
#
#	def publicar(self):
#		self.data_envio = timezone.now()
#		self.save()
#
#		def __str__(self):
#		return 'Assunto: ' + self.assunto + '- Nome: ' + self.nome