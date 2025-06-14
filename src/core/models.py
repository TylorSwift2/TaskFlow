from django.db import models
from django.contrib.auth.hashers import make_password
class Pessoa(models.Model):
    user = models.CharField(max_length=100)
    senha = models.CharField(max_length=255)

    @classmethod
    def registrer(cls, user, senha):
        hashed_password = make_password(senha) 
        pessoa = cls(user=user, senha=senha)
        pessoa.save()
        return pessoa
        
    def __str__(self):
        return f"{self.user} -{self.senha}"