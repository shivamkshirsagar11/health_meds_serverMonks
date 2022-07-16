from . import views
from django.urls import path

urlpatterns = [
    path('', views.login,name='login'),
    path('login', views.auth,name='verify_user'),
    path('register_check', views.register_check,name='register_check'),
    path('register', views.register,name='register'),
]