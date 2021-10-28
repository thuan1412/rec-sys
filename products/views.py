from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


def detail(request):
    print(request.user)
    return HttpResponse(f"You're looking at question {request.user.username}, {request.user.password}")


def homepage(request):
    # TODO: product data here
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/home.html', context)


def productDetail(request, num):
    product = Product.objects.get(id=num)
    context = {
        'product': product
    }
    print(product)
    return render(request, 'products/product-detail.html', context)
