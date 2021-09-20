from products.models import Product
from users.models import User
from django.db import models

class UserProductView(models.Model):
    """Docstring for User. """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
        
