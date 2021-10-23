from django.db import models

class User(models.Model):
    """Docstring for User. """
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username
