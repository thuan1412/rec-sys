import uuid

from django.contrib.auth.forms import UserCreationForm
from django.db.models.aggregates import Avg, Count, Sum
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from recsys.models import ProductRating, UserProductView
from recsys.services import RecSysService, RecSysModel

from .models import Product


def detail(request):
    print(request.user)
    return HttpResponse(f"You're looking at question {request.user.username}, {request.user.password}")


def homepage(request):
    product_count = Product.objects.all().count()
    # join product and productView table, order by view count
    most_viewed_products = Product.objects.values('id', 'name', 'image', 'price').annotate(view_count=Sum('userproductview__count')).filter(view_count__isnull=False).order_by('-view_count')[:4]
    page = request.GET.get('page') or '1'
    page = int(page)
    page_size = request.GET.get('page_size') or '20'
    page_size = int(page_size)
    products = Product.objects.all()[(page-1)*page_size:page*page_size]
    total_pages = int(product_count/page_size) + 1
     
    for product in most_viewed_products:
        product['get_image_url'] = product['image']

    if request.user.is_authenticated:
        recommended_product_ids = RecSysModel.instance().top_item_by_rating(request.user.id)[:4]

        recommended_products = Product.objects.filter(id__in=recommended_product_ids)
    else:
        recommended_products = []

    user = request.user
    context = {
        'products': products[:20],
        'page': page,
        'total_pages': total_pages,
        'product_count': product_count,
        'page_range': range(1, total_pages+1),
        'most_viewed': most_viewed_products,
        'recommended_products': recommended_products,
        'user': user
    }
    return render(request, 'products/home.html', context)


def productDetail(request, num):
    product = Product.objects.get(id=num)

    session = request.session
    rec_session_id = None

    similarity_product_ids = RecSysModel.instance().related_items(num)[:4]
    similarity_products = Product.objects.filter(id__in=similarity_product_ids)
    avg_rating = ProductRating.objects.filter(product_id=product.id).aggregate(Avg('rating'))['rating__avg']
    if avg_rating is None:
        avg_rating = 0
    # print(len(similarity_products))

    try:
        rec_session_id = session['rec_session_id']
    except:
        rec_session_id = str(uuid.uuid4())
        session['rec_session_id'] = rec_session_id

    user = request.user
    product = Product.objects.get(id=num)

    if not product:
        return HttpResponse("Product not found")
    if not user.is_anonymous:
        RecSysService.increase_view_count(user, product)

    # get rating of this product
    rating = None
    if not user.is_anonymous:
        rating = ProductRating.objects.filter(
            product_id=product,
            user_id=user
        ).first()
        if rating:
            rating = rating.rating

    context = {
        'product': product,
        'similarity_products': similarity_products,
        'rating': rating,
        'avg_rating': avg_rating,
    }
    return render(request, 'products/product-detail.html', context)

def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'products': products
    }
    return render(request, 'products/search.html', context)


def rating(request, id):
    product_id = id
    rating = request.POST.get('rating') 
    user = request.user
    user_id = user.id

    product = Product.objects.get(id=product_id)

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
                user_id=user,
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
    return redirect(f"/{product_id}")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'products/signup.html'
