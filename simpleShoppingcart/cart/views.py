from django.shortcuts import render

# Create your views here.
def display_items(request):
    return render(request,'display_items.html',{})

def display_cart(request):
    return render(request,'display_cart.html',{})