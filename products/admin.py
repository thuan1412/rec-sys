from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from .models import Product


class ProductAdmin(admin.ModelAdmin, DynamicArrayMixin):
    fields = ['name', 'price', 'quantity', 'image', 'description', 'properties']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return obj.image_tag

    def get_description(self, obj):
        return obj.get_description()

    get_description.allow_tags = True
    image_tag.allow_tags = True

    search_fields = ['name']
    filter_fields = ['price']

    list_display = ('name', 'price', 'description')


admin.site.register(Product, ProductAdmin)
