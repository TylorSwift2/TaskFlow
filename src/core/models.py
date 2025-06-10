from django.db import models
class Pessoa(models.Model):
    user = models.CharField(max_length=100)
    senha = models.IntegerField()

    @classmethod
    def registrer(cls, user, senha):
        pessoa = cls(user=user, senha=senha)
        pessoa.save()
        return pessoa
        
    def __str__(self):
        return self.user