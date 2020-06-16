from django.db import models
from django.contrib import auth
import random
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect,HttpResponse
# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return self.username
class Category(models.Model):
    product_category=models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.product_category
class Product(models.Model):
    name=models.CharField(null=True,blank=True,max_length=80)
    category=models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    price=models.DecimalField(decimal_places=2,max_digits=100000)
    photo=models.ImageField(null=True,blank=True,upload_to='productimages/')
    discription=models.CharField(null=True,blank=True,max_length=400)
    color=models.CharField(null=True,blank=True,max_length=20)
    def __str__(self):
        return self.name
status_choice=(
('confirmed','confirmed'),
('pending','pending'),
)
class EmailVerified(models.Model):

    user=models.OneToOneField(auth.models.User,on_delete=models.CASCADE)
    unique_number=models.PositiveIntegerField(default=0,unique=True)
    status=models.CharField(choices=status_choice,default='pending',max_length=20)
    def __str__(self):
        return self.user.username
status_delivery=(
('pending','pending'),
('delivered','delivered'),
('shiped','shiped')
)
class Order(models.Model):
    order_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    user=models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
    Address=models.CharField(max_length=200)
    phone=models.PositiveIntegerField()
    pincode=models.IntegerField()
    status=models.CharField(choices=status_delivery,max_length=20,default='pending')
    def __str__(self):
        return self.product.name+'-'+str(self.quantity)
    def save(self,*args,**kwargs):
        us=EmailVerified.objects.get(user=self.user)
        if str(us.status)=='confirmed':
            super(Order,self).save(*args,**kwargs)
class FeedBack(models.Model):
    user=models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=250)
    def __str__(self):
        return self.user.username
