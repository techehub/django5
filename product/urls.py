
from django.contrib import admin
from django.urls import path
from .views import myProducts, productlist, addItem

urlpatterns = [

    path('product/<str:pid>',  myProducts ),
    path('items', productlist),
    path ('addItem', addItem)


]
