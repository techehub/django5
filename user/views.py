from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail

def signup (req):

    if req.method=="GET":

        template = loader.get_template("signup.html")

        data = {
        }
        res = template.render(data, req)
        return HttpResponse(res)

    else :
        template = loader.get_template("signup_success.html")

        data = {
            "vals" : req.POST
        }

        res = template.render(data, req)
        return HttpResponse(res)

