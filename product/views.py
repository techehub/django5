from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Product

def productlist (req):

    #p_id = req.COOKIES ['productid']
    p_id = req.COOKIES.get ('productid',"NA")
    print("PID is ", p_id)

    template = loader.get_template("prodlist.html")

    items = Product.objects.all()


    data = {
        "products" : items,
        "browsed_products" : p_id
    }
    res = template.render(data, req)
    return HttpResponse(res)


def myProducts(req, pid):



    template = loader.get_template("product.html")
    item = Product.objects.get (id = pid)
    data = {

        "product" : item

    }
    res = template.render(data, req)
    httpResponse = HttpResponse(res)


    p_ids = req.COOKIES['productid']
    if p_ids:
        p_ids= p_ids + "|" +pid
    else :
        p_ids = pid


    max_age = 365 * 24 * 60 * 60
    httpResponse.set_cookie("productid" , p_ids, max_age  )
    return httpResponse

def addItem (request):
    pid = request.GET ['pid']
    qty = request.GET['qty']

    cartItems = {}

    if request.session.__contains__("cart"):
        cartItems = request.session['cart']

    cartItems[pid] = qty
    request.session['cart'] = cartItems
    print(request.session['cart'])
    return HttpResponse("Added Item to Cart")


def viewCart (request):
    template = loader.get_template("cart.html")
    if request.session.__contains__("cart"):
        cartItems = request.session['cart']

        items= []
        for x,y in cartItems.items():
            p =Product.objects.get(id=x)
            items.append ({"id": x,
                            "qty": y,
                            "name": p.name ,
                            "price": p.price,
                            "total" : p.price * int(y)
                            })

        data ={"products": items}

        res = template.render(data, request)
        return HttpResponse(res)
    else :
        return HttpResponse("Your Cart is Empty")


def search (request):
    template = loader.get_template("search.html")
    data = {

    }
    res = template.render(data, request)
    return HttpResponse(res)

def mypruduct (request):
    vals = {
        "id": 123,
        "name": "OPPO"
    }
    return JsonResponse(data=vals)