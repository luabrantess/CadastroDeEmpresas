from pyexpat import model
from re import M
from django.db import models 

class Cidade(models.Model):
   
    municipio = models.CharField(max_length=20, null=True)
    uf = models.CharField(max_length=5, null=True)
   

class Area(models.Model):
  
    area = models.CharField(max_length=20, null=False)



class Empresa(models.Model):

    nome = models.CharField(max_length=100, null=False)
    cidade = models.TextField(null=False)
    endereco = models.CharField(max_length=100, null=False)
    descricao = models.TextField(null=False)
    descricao_ingles = models.TextField(max_length=200, null=True)
    slogan = models.TextField(max_length=100, null=True)
    ponto_contato = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=False)
    site = models.CharField(max_length=50, null=True)
    

    def __str__(self):
        return self.nome 


class Produto(models.Model):
    ident = models.ForeignKey('Empresa', null=False, on_delete=models.PROTECT)
    produto = models.TextField(null=False)

class Telefone(models.Model):
    ident = models.ForeignKey('Empresa', null=False,on_delete=models.PROTECT)
    telefone = models.BigIntegerField(null=False)
