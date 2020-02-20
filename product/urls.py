
from django.contrib import admin
from django.urls import path
from .views import myProducts, productlist, addItem, viewCart, search, mypruduct

urlpatterns = [

    path('product/<str:pid>',  myProducts ),
    path('items', productlist),
    path ('addItem', addItem),
    path ('viewCart', viewCart),
    path('search', search),
    path ('mypruduct', mypruduct)


]
