from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class AddProductModel(models.Model):
    product_name = models.CharField(max_length = 100)
    product_description = models.CharField(max_length = 500)
    product_price = models.DecimalField(decimal_places=2,max_digits=10)

#to be worked on
class AddToCartModel(models.Model):
    id = models.AutoField(primary_key = True)
    product_Id = models.CharField(max_length = 100)
    product_name = models.CharField(max_length = 100)
    product_description = models.CharField(max_length = 500)
    product_price = models.DecimalField(decimal_places=2,max_digits=10)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length = 150)
    ordered_products = models.ManyToManyField(AddProductModel,blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save,sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class OrderItem(models.Model):
    product = models.OneToOneField(AddProductModel,on_delete=models.SET_NULL,null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.product_name

class Order(models.Model):
    ref_code = models.CharField(max_length=15)    
    owner = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()
    def get_cart_total(self):
        return sum([item.product.product_price for item in self.items.all()])

        def __str__(self):
            return '{0} - {1}'.format(self.owner,self.ref_code)