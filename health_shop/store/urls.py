from . import views
from django.urls import path

urlpatterns = [
    path('', views.login,name='login'),
    path('login', views.auth,name='verify_user'),
    path('register_check', views.register_check,name='register_check'),
    path('register', views.register,name='register'),
    path('load_cart', views.open_cart,name='load_cart'),
    path('addprod', views.addProduct,name='add_prod'),
    path('<id>/shop_single',views.shop_single,name='shop_sinlge'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='cabout'),
    path('rmprod',views.rmprod,name='rmprod'),
    path('logout',views.logout,name='logout'),
    path('checkout',views.checkout,name='checkout'),
    path('ty',views.ty,name='ty'),
    path('<category>/shop',views.shop,name='shop'),
    path('shop',views.shop1,name='shop1'),
    
    

    # path('history',views.history,name='history'),
]