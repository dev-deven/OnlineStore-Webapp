
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Contact
from math import ceil
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.

def index(request):


    #params = {'no_of_slides':nSlides , 'range': range(1,nSlides) ,'product': products }
    #allProds = [[products, range(1,nSlides) , len(products)],
    #            [products, range(1,nSlides) , len(products)]]
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n // 4 + (ceil((n / 4) - (n // 4)))
        allProds.append([prod,range(1,nSlides),len(prod)])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html',params)



def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request , 'shop/tracking.html')


def search(request):
    return HttpResponse("Yoy are in search Section ;)")

def productview(request , myid):
    # Featch The product using id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodview.html' , {'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')
