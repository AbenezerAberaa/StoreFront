from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

def say_Hello(request):
    products = Product.objects.filter(title__icontains = "coffee")

    

    return render(request, 'hello.html', {"name": "Abeny", "products": list(products)})


