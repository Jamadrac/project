from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from store.models import Product

def frontpage(request):
      #return httpresponse(dfghjklkjhgfd)
    products = Product.objects.filter(status=Product.ACTIVE)[0:6]
