from django.shortcuts import render

from store.models import Product

def frontpage(request):
      #return httpresponse(dfghjklkjhgfd)
    products = Product.objects.filter(status=Product.ACTIVE)[0:6]

    return render(request, 'core/frontpage.html', {
        'products': products
    })

def about(request):
    #return httpresponse(dfghjklkjhgfd)
    return render(request, 'core/about.html')