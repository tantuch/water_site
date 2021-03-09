#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Company
from .models import Contacts
from .models import Products
from .models import Sertify


def website(request):
    company = Company.objects.all()
    contacts = Contacts.objects.all()
    # Groups by N-product
    N = 3
    products = Products.objects.all()
    groups_products = [products[k:k+N] for k in range(0, len(products), N)]
    sertify = Sertify.objects.all()

    template = loader.get_template('index.html')
    context = {
        'company': company,
        'contacts': contacts,
        'groups_products': groups_products,
        'sertify': sertify,
    }
    return HttpResponse(template.render(context, request))


def webadmin(request):
    return HttpResponse("I'm webadmin")
