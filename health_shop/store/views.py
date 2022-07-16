from django.shortcuts import render,redirect
from store.models import Auth_User as au,Product as p

def login(request):
    return render(request, 'login.html')

def auth(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = au.objects.filter(email=email, password=password).first()
        if user:
            products = p.get_all_products()
            return render(request, 'home.html',{"products":products})
        else:
            return render(request, 'login.html',{"msg":"user not found!!"})

def register(request):
    return render(request, 'register.html')

def register_check(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        user = au.objects.filter(email=email).first()
        if user:
            return render(request, 'register.html',{"msg":"Email already registered!!"})
        else:
            user = au(email=email,password=password,name=name,phone=phone,address=address)
            user.save()
            return render(request, 'login.html',{"msg":"Registration successful!"})
       
