import uuid

from django.contrib.auth.forms import UserCreationForm
from django.db.models.aggregates import Count, Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from recsys.models import UserProductView
from recsys.services import RecSysService, RecSysModel

from .models import Product


def detail(request):
    print(request.user)
    return HttpResponse(f"You're looking at question {request.user.username}, {request.user.password}")


def homepage(request):
    products = Product.objects.all()
    # join product and productView table, order by view count
    most_viewed_products = Product.objects.values('id', 'name', 'image', 'price').annotate(view_count=Sum('userproductview__count')).filter(view_count__isnull=False).order_by('-view_count')[:3]
     
    for product in most_viewed_products:
        product['get_image_url'] = product['image']

    recommened_product_ids = RecSysModel.instance().top_item_by_rating(request.user.id)

    recommended_products = Product.objects.filter(id__in=recommened_product_ids)

    user = request.user
    context = {
        'products': products[:20],
        'most_viewed': most_viewed_products,
        'recommended_products': recommended_products,
        'user': user
    }
    return render(request, 'products/home.html', context)


def productDetail(request, num):
    product = Product.objects.get(id=num)
    context = {
        'product': product
    }

    session = request.session
    rec_session_id = None

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

    return render(request, 'products/product-detail.html', context)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'products/signup.html'
