from django.db import models
from django.utils.html import format_html
from django.conf import settings

from storages.backends.s3boto3 import S3Boto3Storage

class PublicMediaStorage(S3Boto3Storage):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    file_overwrite = False

class Product(models.Model):
    """Product model"""
    name = models.CharField(max_length=100)
    price = models.FloatField()
    # TODO: array image
    image = models.FileField(storage=PublicMediaStorage)

    @property
    def image_tag(self):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(self.image))

    # image_tag.short_description = 'Image'
    # image_tag.allow_tags = True

    def __str__(self):
        return self.name
    
