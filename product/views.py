from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Product

def productlist (req):
    template = loader.get_template("prodlist.html")

    items = Product.objects.all()


    data = {
        "products" : items
    }
    res = template.render(data, req)
    return HttpResponse(res)


def myProducts(req, aaa):
    template = loader.get_template("product.html")
    item = Product.objects.get (id = aaa)
    data = {

        "product" : item

    }
    res = template.render(data, req)
    return HttpResponse(res)

    #return HttpResponse ("This is my products page")