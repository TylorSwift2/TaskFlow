from django.db import models
from django.contrib.auth.hashers import make_password

class Pessoa(models.Model):
    """
    Model representing a user (Pessoa) in the system.
    Fields:
        user: Username of the person.
        senha: Hashed password.
        email: Email address.
    """
    user = models.CharField(max_length=100)
    senha = models.CharField(max_length=255)
    email = models.EmailField(max_length=355)

    @classmethod
    def registrer(cls, user, password, email):
        """
        Registers a new user.
        Hashes the password before saving the user to the database.
        Returns the created Pessoa instance.
        """
        hashed_password = make_password(password)
        pessoa = cls(user=user, senha=hashed_password, email=email)
        pessoa.save()
        return pessoa
        
    def __str__(self):
        """
        Returns a string representation of the Pessoa object.
        """
        return f"{self.user} -{self.senha}"