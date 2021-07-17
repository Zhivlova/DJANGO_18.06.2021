from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'магазин'

    products = Product.objects.all()[:3]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'new_shop/index.html', context=context)

def contacts(request):
    return render(request, 'new_shop/contact.html')