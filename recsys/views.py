from django.http import JsonResponse

from products.models import Product
from recsys.models import ProductRating


def rate_product(request):
    product_id = request.GET.get('product_id')
    user_id = request.GET.get('user_id')
    rating = request.GET.get('rating') 
    print({
        'product_id': product_id,
        'user_id': user_id
    })

    product = Product.objects.get(id=product_id)

    user = request.user
    if  user:
        rating_record = ProductRating.objects.filter(
            product_id=product_id,
            user_id=user_id
        ).first()
        if rating_record:
            rating_record.rating = rating
            rating_record.save()
        else:
            ProductRating.objects.create(
                product_id=product,
                user_id=user_id,
                rating=rating
            )
    else:
        rating_record = ProductRating.objects.filter(
            product_id=product_id,
            user_id=user_id
        ).first()
        ProductRating.objects.create(
            product_id=product,
            user_id=user,
            rating=rating
        )
    return JsonResponse({"status": "ok"})
