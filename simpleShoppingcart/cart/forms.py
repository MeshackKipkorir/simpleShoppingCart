from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AddProductModel

class addProductForm(forms.ModelForm):
    class Meta:
        model = AddProductModel
        fields = ('product_name','product_description','product_price')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length=300)
    email = forms.EmailField(max_length=150)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)
