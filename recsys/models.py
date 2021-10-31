from products.models import Product
from users.models import User
from django.db import models

class UserProductView(models.Model):
    """Docstring for User. """
    user_id = models.IntegerField(default=None, blank=True, null=True)
    product_id = models.IntegerField(default=None, blank=True, null=True)
    session_id = models.CharField(max_length=20, default=None, blank=True, null=True)
    count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user_id} - {self.product_id} - {self.session_id}"
        
class ProductRating(models.Model):
    """Docstring for User. """
    user_id = models.IntegerField(default=None, blank=True, null=True)
    product_id = models.IntegerField(default=None, blank=True, null=True)
    session_id = models.CharField(max_length=20, default=None, blank=True, null=True)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.user_id} - {self.product_id} - {self.session_id}"
