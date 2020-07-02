from django.shortcuts import redirect, render
from django.http import HttpResponse
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
#        context = {'name'name, 'email':email, 'subject':subject, 'message':message}
       messages.error(request, 'your form is not submitted')
       return render(request, "contact.html", context)

           

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


def search(request):
    queryset_list = Product.objects.order_by('date')
    product = Product.objects.all()
    data = request.GET['keywords']
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(details__icontains=keywords) | Q(name__icontains=keywords))
            if queryset_list:
                return render(request, 'search.html', {'search':queryset_list})
            else: 
                return render(request, 'search.html', {'search':product, 'error':f'No match found "{data}" try keysword(motherboard, monitor, camera...)', 'data':data})
    else:
        return render(request, 'search.html', {'search':product})

def product(request, id):
    product = Product.objects.get(id=id)
    category = Product.objects.all().filter(category=product.category)
    context = {
        'product':product,
        'category':category
    }
    
    return render(request, 'product-details-affiliate.html', context)

def accesspoint(request):
    accesspoint = Product.objects.all().filter(category='accesspoint')
    return render(request, 'accesspoint.html', {'accesspoint':accesspoint})


def desktop(request):
    desktop = Product.objects.all().filter(category='desktop')
    return render(request, 'desktop.html', {'desktop':desktop})

def monitor(request):
    monitor = Product.objects.all().filter(category='monitor')
    return render(request, 'monitor.html', {'monitor':monitor})

def motherboard(request):
    motherboard = Product.objects.all().filter(category='motherboard')
    return render(request, 'motherboard.html', {'motherboard':motherboard})

def camera(request):
    camera = Product.objects.all().filter(category='camera')
    return render(request, 'camera.html', {'camera':camera})
