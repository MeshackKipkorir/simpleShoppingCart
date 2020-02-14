from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate
from .models import AddProductModel,AddToCartModel,Profile,Order,OrderItem
from .forms import addProductForm,SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        user_profile = get_object_or_404(Profile, user=request.user)

        items = Order.objects.filter(owner = user_profile)
        
        return render(request,'display_cart.html',{'items':items})

def add_product(request):
    form = addProductForm()
    if request.method == "POST":
        form = addProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = addProductForm()
        
    
    return render(request,'add_products.html',{'form':form})

@login_required
def add_to_cart(request,**kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = AddProductModel.objects.filter(id=kwargs.get('item_id',"")).first()
    if product in request.user.profile.ordered_products.all():
        messages.info(request, 'Product already added to cart')
        return redirect('display_items')
    #create order item
    order_item,status = OrderItem.objects.get_or_create(product=product)
    #create order
    user_order,status = Order.objects.get_or_create(owner=user_profile)
    user_order.items.add(order_item)
    if status:
        # user_order.ref_code = generate_order_id()
        user_order.save()
    messages.info(request,'item added to cart')
    return redirect('display_cart')
