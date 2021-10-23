from django.contrib import admin

from recsys.models import ProductRating

# Register your models here.

class ProductRatingAdmin(admin.ModelAdmin):
    fields = ['user_id', 'product_id','rating']

admin.site.register(ProductRating, ProductRatingAdmin)