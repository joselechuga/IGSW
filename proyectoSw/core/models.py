from django.db import models

# Create your models here.
class nuevoUsuario(models.Model):
    nombreUsuario = models.CharField(max_length=50)
    psw = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    edad=models.IntegerField()
    genero=models.CharField(max_length=1)

