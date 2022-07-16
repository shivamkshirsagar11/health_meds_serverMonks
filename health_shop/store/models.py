from unicodedata import category
from django.db import models

class Auth_User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    photo = models.ImageField(upload_to="user_profile",default="user_profile/default.png")

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    discription=models.CharField(max_length=100,default='',null=True,blank=True)
    price=models.IntegerField()
    category=models.CharField(max_length=100)
    image=models.ImageField(upload_to='product_details',default="user_profile/default.png")
 
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    def get_products_by_id(category_name):
        if category_name:
            return Product.objects.filter(category=category_name)
        else:
            return Product.objects.all()




