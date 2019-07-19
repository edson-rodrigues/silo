from django.db import models

# Create your models here.
class Paciente(models.Model):
	paciente_nome = models.CharField(max_length=50)
	paciente_cpf = models.CharField(max_length=15)
	
