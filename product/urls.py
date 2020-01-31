
from django.contrib import admin
from django.urls import path
from .views import myProducts, productlist

urlpatterns = [

    path('product/<str:aaa>',  myProducts ),
    path('items', productlist),


]
