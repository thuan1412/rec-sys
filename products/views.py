from django.shortcuts import render
from django.http import HttpResponse

from recsys.services import RecSysService
import uuid
from .models import Product


def detail(request):
    print(request.user)
    return HttpResponse(f"You're looking at question {request.user.username}, {request.user.password}")


def homepage(request):
    # TODO: product data here
    products = Product.objects.all()

    context = {
        'products': products,
        'most_viewed': products[:3],
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

    print(session.items())
    RecSysService.increase_view_count(1, 1)

    return render(request, 'products/product-detail.html', context)
