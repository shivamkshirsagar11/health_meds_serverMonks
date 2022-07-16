from django.contrib import admin
from store.models import Auth_User,Product,Cart_generator,Cart_Item

admin.site.register(Auth_User)
admin.site.register(Product)
admin.site.register(Cart_generator)
admin.site.register(Cart_Item)
