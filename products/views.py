from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from recsys.services import RecSysService

import uuid
from .models import Product


def detail(request):
    print(request.user)
    return HttpResponse(f"You're looking at question {request.user.username}, {request.user.password}")


def homepage(request):
    # TODO: product data here
    products = Product.objects.all()
    user = request.user

    context = {
        'products': products[:20],
        'most_viewed': products[:3],
        'user': user
    }
    print(user.id)

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

    print(user, product)
    if not product:
        return HttpResponse("Product not found")
    RecSysService.increase_view_count(user, product)

    return render(request, 'products/product-detail.html', context)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'products/signup.html'
