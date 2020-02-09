from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.display_items,name="display_items"),
    path('display_cart/',views.display_cart,name="display_cart")
]
