from django.shortcuts import render,redirect
from store.models import Auth_User as au,Product as p,Cart_generator as cg

def login(request):
    return render(request, 'login.html')

def auth(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = au.objects.filter(email=email, password=password).first()
        if user:
            products = p.get_all_products()
            global userID
            userID = user.id
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
       
def load_cart(request):
    cartObj = cg.get_cart(userID)
    if cartObj is None:
        return render(request, 'cart.html',{"msg":"Nothing in cart right now"})
    else:
        cartItems = cg.get_cart_items(cartObj.cart_no)
        return render(request, 'cart.html',{"cart_items":cartItems})