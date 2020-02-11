from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .models import AddProductModel,AddToCartModel
from .forms import addProductForm,SignUpForm

# Create your views here.
def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username = username,password = password)
        login(request,user)
        return redirect('display_items')

    return render(request,'signup.html',{'form':form})
    

def display_items(request):
    items = AddProductModel.objects.all()
    context = {
        'items': items
    }
    return render(request,'display_items.html',context)

def display_cart(request):

    return render(request,'display_cart.html',{})

def add_product(request):
    form = addProductForm()
    if request.method == "POST":
        form = addProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = addProductForm()
        
    
    return render(request,'add_products.html',{'form':form})