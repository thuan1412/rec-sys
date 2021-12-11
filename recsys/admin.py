from django.contrib import admin
from django.db.models.aggregates import Count, Sum
from django.db.models.expressions import Window
from products.models import Product

from recsys.models import ProductRating, UserProductView

# Register your models here.


class ProductRatingAdmin(admin.ModelAdmin):
    fields = ['user_id', 'product_id', 'rating', 'session_id']
    list_display = ('user_id', 'product_id', 'rating', 'session_id')


class UserProductViewGroupBy(UserProductView):
    class Meta:
        proxy = True


class ProductViewAdmin(admin.ModelAdmin):
    fields = ['user_id', 'product_id', 'count', 'session_id']
    list_display = ('user_id', 'product_id', 'count', 'session_id')


class UserProductViewGroupByAdmin(admin.ModelAdmin):
    fields = ['product_id', 'total']
    list_display = ('product_id', 'total')


    ordering = ('product_id', )

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            total=Window(
                expression=Sum('count'),
                partition_by=['product_id'],
                order_by=['product_id']
            )
        )

    def total(self, obj):
        print(UserProductViewGroupBy.objects.values('product_id').annotate(count=Count('id')).order_by())
        return obj.total

admin.site.register(ProductRating, ProductRatingAdmin)
admin.site.register(UserProductView, ProductViewAdmin)
admin.site.register(UserProductViewGroupBy, UserProductViewGroupByAdmin)
