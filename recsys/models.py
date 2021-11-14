from products.models import Product
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

class UserProductView(models.Model):
    """Docstring for User. """
    user_id = models.ForeignKey(User, on_delete=CASCADE, default=None, blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=20, default=None, blank=True, null=True)
    count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user_id} - {self.product_id} - {self.session_id}"
        
class ProductRating(models.Model):
    """Docstring for User. """
    user_id = models.ForeignKey(User, on_delete=CASCADE, default=None, blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=20, default=None, blank=True, null=True)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.user_id} - {self.product_id} - {self.session_id}"
