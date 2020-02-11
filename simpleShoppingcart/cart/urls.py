from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.display_items,name="display_items"),
    path('signup',views.signup),
    path('display_cart/',views.display_cart,name="display_cart"),
    path('add_product/',views.add_product,name="add_product"),
]
