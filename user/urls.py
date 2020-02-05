
from django.contrib import admin
from django.urls import path
from .views import contactus, contactSave

urlpatterns = [


    path('contactus', contactus),
    path ('contactSave', contactSave)


]
