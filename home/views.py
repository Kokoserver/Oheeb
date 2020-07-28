from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
=======
from django.db.models import Q
from .models import Product, Cart
from customer.models import Contact
from django.contrib import messages
def home(request):
    camera = Product.objects.all().filter(category='camera')[4:]
    accesspoint = Product.objects.all().filter(category='accesspoint')[4:]
    monitor = Product.objects.all().filter(category='monitor')[4:]
    topRated = Product.objects.all()
    motherboard = Product.objects.all().filter(category='motherboard')[4:]
    desktop = Product.objects.all().filter(category='desktop')[4:]
    switch = Product.objects.all().filter(category='switch')
    router = Product.objects.all().filter(category='router')
    context = {'camera':camera,
               'monitor':monitor,
               'motherboard':motherboard,
               'desktop':desktop,
               'accesspoint':accesspoint,
               'router':router,
               'switch':switch,
               'topRated':topRated
               
               }
    
    return render(request, "index.html", context)

def contact(request):
    if request.method == 'POST':
       name =  request.POST['name']
       email = request.POST['email']
       subject = request.POST['subject']
       message = request.POST['message']
       contact = Contact(name=name, email=email, subject=subject, message=message)
       contact.save()
       messages.success(request,'your form is submitted')
       return render(request, "index.html")
    else:
       # messages.error(request, 'your form is not submitted')
       return render(request, "contact.html")
    
    

           

def cart(request, id):
    try:
        if request.user.is_authenticated:
             product = Product.objects.get(id=id)
             if Cart.objects.filter(product=product).exists():
                 messages.error(request, 'You have this product in your cart')
                 return redirect('dashboard')
             else:
                 prodt = Cart(product=product, user=request.user.id, status='pending', is_owned=False)
                 prodt.save()
                 carts = Cart.objects.filter(user=request.user.id)
                 messages.success(request, 'your product is added to your cart, we will contact you')
                 return render(request, 'dashboard.html', {'carts':carts} )
        elif not request.user.is_authenticated:
                 messages.error(request, 'Please login to add product to cart')
                 return redirect('login')   
    except ValueError as identifier:
             return redirect('home')
        

def about(request):
    return render(request, "about-us.html")

>>>>>>> e7df72d1b339a5208491e4f109f470d248a9b24e

def home(request):
    return render(request, "index.html")


def view(request, id):
    return HttpResponse(id)