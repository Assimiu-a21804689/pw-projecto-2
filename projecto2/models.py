from django.db import models

# Create your models here.

class Contacto(models.Model):
    nome = models.CharField(max_length=40)
    apelido = models.CharField(max_length=40)
    imail = models.EmailField()
    contacto = models.CharField(max_length=9)
    dataNas = models.CharField(max_length=8)

class Encomendar(models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    dataNascimento = models.DateField();
    telefone = models.CharField(max_length=9)
    email = models.EmailField()
    morada = models.CharField(max_length= 40)
    codigo_postal = models.CharField(max_length= 50)
    quantidade = models.IntegerField()
    def __str__(self):
        return f"{self.nome} {self.apelido}"

class Sobre (models.Model):
    sugestao = models.TextField()

    def __str__(self):
        return self.sugestao[:30]
