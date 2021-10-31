from django.contrib import admin

from recsys.models import ProductRating, UserProductView

# Register your models here.


class ProductRatingAdmin(admin.ModelAdmin):
    fields = ['user_id', 'product_id', 'rating', 'session_id']
    list_display = ('user_id', 'product_id', 'rating', 'session_id')


class ProductViewAdmin(admin.ModelAdmin):
    fields = ['user_id', 'product_id', 'count', 'session_id']
    list_display = ('user_id', 'product_id', 'count', 'session_id')


admin.site.register(ProductRating, ProductRatingAdmin)
admin.site.register(UserProductView, ProductViewAdmin)
