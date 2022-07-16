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
