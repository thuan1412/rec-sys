from django.db import models
from django.utils.html import format_html


class Product(models.Model):
    """Product model"""
    name = models.CharField(max_length=100)
    price = models.FloatField()
    # TODO: array image
    image = models.ImageField(upload_to='uploads')

    @property
    def image_tag(self):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(self.image))

    # image_tag.short_description = 'Image'
    # image_tag.allow_tags = True

    def __str__(self):
        return self.name
    
