from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from .models import Contact

def contactus (request):

    template = loader.get_template("contact.html")
    data = {}
    res=template.render ( data, request )
    return HttpResponse(res)



def contactSave (req):

    c = Contact(
        fname= req.POST["firstname"],
        lname=req.POST["lastname"],
        email=req.POST["email"],
        phone=req.POST["phone"],
        msg=req.POST["message"],
    )

    c.save()

    template = loader.get_template("contactSuccess.html")
    data = {}
    res = template.render(data, req)
    return HttpResponse(res)

