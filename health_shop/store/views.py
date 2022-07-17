from urllib import request
from django.http import JsonResponse
from django.shortcuts import render,redirect
from store.models import Auth_User as au,Product as p,Cart_generator as cg,Cart_Item as ci
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
global userID
userID = -1
def login(request):
    return render(request, 'login.html')

def auth(request):
    global userID
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = au.objects.filter(email=email, password=password).first()
        if user:
            products = p.get_all_products()
            userID = user.id
            return render(request, 'home.html',{"products":products})
        else:
            return render(request, 'login.html',{"msg":"user not found!!"})
    else:
        products = p.get_all_products()
        if userID != -1:return render(request, 'home.html',{"products":products})
        return render(request, 'login.html',{"msg":"Sme error occured!!"})

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
       
def open_cart(request):
    cartObj = cg.get_cart(userID)
    if cartObj is None:
        return render(request, 'cart.html',{"msg":"Nothing in cart right now"})
    else:
        grand_total(request)
        cartObj = cg.get_cart(userID)
        cartItems = cg.get_cart_items(cartObj.cart_id)
        if len(cartItems) == 0:
            cartObj.delete()
            cartItems.delete()
            return render(request, 'cart.html',{"msg":"Nothing in cart right now"})
        return render(request, 'cart.html',{"cart_items":cartItems,"cart_gen":cartObj})

def shop_single(request,id):
    context={}
    context["product"]=p.objects.get(id=id)
    return render(request,'shop-single.html',context)

def about(request):
    return render(request,'about.html')

# def about(request):
#     return render(request,'history.html')

def contact(request):
    return render(request,'contact.html')
@csrf_exempt
def addProduct(request):
    global userID
    if userID == -1:return render(request, 'login.html',{"msg":"Some error occured!!"})
    elif request.method == 'POST':
        prod_id = request.POST['id']
        total = request.POST['tot']
        cartObj = cg.get_cart(userID)
        if cartObj is None:
            cart_id_generated = cg.generate_cart()
            cart_gen_obj = cg(cart_id = cart_id_generated,user_id = userID)
            cart_gen_obj.save()
            prod_temp = p.get_products_by_id(prod_id)
            cart_item_obj = ci(cart_no = cart_id_generated,product_name = prod_temp.name,product_price = prod_temp.price,total_ord = total,product_id = prod_id,image = prod_temp.image,total_price=int(prod_temp.price)*int(total))
            cart_item_obj.save()
        else:
            cartObj = cg.get_cart(userID)
            itemObj = ci.objects.filter(Q(cart_no = cartObj.cart_id) & Q(product_id = prod_id)).first()
            if itemObj is not None:
                itemObj.total_ord = int(itemObj.total_ord) + int(total)
                itemObj.total_price = int(itemObj.product_price)*int(itemObj.total_ord)
                itemObj.save()
            else:
                prod_temp = p.get_products_by_id(prod_id)
                cart_item_obj = ci(cart_no = cartObj.cart_id,product_name = prod_temp.name,product_price = prod_temp.price,total_ord = total,product_id = prod_id,image = prod_temp.image,total_price = int(prod_temp.price)*int(total))
                cart_item_obj.save()
    return JsonResponse({"Done":"Done"})

@csrf_exempt
def rmprod(request):
    if request.method == "POST":
        pid = request.POST['id']
        cartObj = cg.get_cart(userID)
        if cartObj:
            item = ci.objects.get(Q(cart_no = cartObj.cart_id) & Q(product_id = pid))
            item.delete()
    return JsonResponse({"Done":"Done"})

def logout(request):
    global userID
    userID = -1
    return render(request,'login.html',{"msg":"logout successfull!"})

def checkout(request):
    grand_total(request)
    cartObj = cg.get_cart(userID)
    items = cg.get_cart_items(cartObj.cart_id) 
    return render(request,'checkout.html',{"cart_gen":cartObj,"cart_items":items})

def grand_total(request):
    cartObj = cg.get_cart(userID)
    items = cg.get_cart_items(cartObj.cart_id)
    tot = 0
    for i in items:
        tot = tot+int(i.total_price)
    cartObj.total_of_cart = tot
    cartObj.save()

def ty(request):
    cartObj = cg.get_cart(userID)
    cartItems = cg.get_cart_items(cartObj.cart_id)
    cartObj.delete()
    cartItems.delete()
    return render(request,'thankyou.html')

def shop(request,category):
    
    if category:
         products=p.objects.filter(category=category)
         return render(request,'shop.html',{"products":products,"cat":1})
    else:
        products = p.get_all_products()
        return render(request,'shop.html',{"products":products})

def shop1(request):
    products = p.get_all_products()
    return render(request,'shop.html',{"products":products})


def history(request):
    return render(request,'history.html')
   

    


