from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
           try:
                auth.login(request, user)
                messages.success(request, f'you are Login {username}')
                return redirect('dashboard')
           except 'error' as identifier:
               messages.error(request, 'Please retry')
        else:
            messages.error(request, 'Invalid credential')
            return redirect('login')
    else:
       return render(request,'login.html')

def register(request):
    if request.method == "POST":
        # getting the form value
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        context = {
            'firstName':firstName,
            'lastName':lastName,
            'email':email,
            'username':username,
        }
        #check if the password match
        if password == confirmPassword:
            #check if username exist
            if User.objects.filter(username=username).exists():
                messages.error(request, ' That username is taken')
                return render(request,"register.html", context)
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, ' That email is being used')
                    return render(request,"register.html", context)
                else:
                    #create the user
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=firstName, last_name=lastName)
                    #loging the user
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('home')
                    user.save()
                    messages.success(request, 'You are now registered and can login')
                    return redirect('login')
                    
                    
        else:
            messages.error(request, 'Password do not match')
            return render(request,"register.html", context)
    else:
        return render( request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect("home")

def helpCenter(request):
     if request.method == "POST":
            # getting the form value
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        newPassword = request.POST['newPassword']
        confirmPassword = request.POST['confirmPassword']
        context = {
            'firstName':firstName,
            'lastName':lastName,
            'email':email,
            'username':username,
        }
        #check if the password match
        if newPassword == confirmPassword:
            #check if username exist
            user = User.objects.get(username=username)
            user.set_password(newPassword)
            messages.success(request, ' password change successfully')
            return render(request,"dashboard.html", context)
        else:
            messages.error(request, 'Password do not match')
            return render(request,"dashboard.html", context)
     else:
        return render( request, "dashboard.html")



def dashboard(request):
    return render(request, "dashboard.html")