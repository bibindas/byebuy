from django.contrib import admin
from .models import Brand,Product,Item,Colour,Category,Image
# Register your models here.

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Item)
admin.site.register(Colour)
admin.site.register(Category)
admin.site.register(Image)