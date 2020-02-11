from django.contrib import admin
from .models import AddProductModel,AddToCartModel,Profile
# Register your models here.

admin.site.register(AddProductModel)
admin.site.register(AddToCartModel)
admin.site.register(Profile)