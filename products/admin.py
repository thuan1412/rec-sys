from django.contrib import admin
from django.utils.html import format_html

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price','image', 'image_tag']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return obj.image_tag
    image_tag.allow_tags = True

    search_fields = ['name']
    filter_fields = ['price']

    list_display = ('name', 'price', 'image_tag')


admin.site.register(Product, ProductAdmin)
