from django.contrib import admin
from eapp.models import Product,Category,EmailVerified,Order,FeedBack
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(EmailVerified)
admin.site.register(Category)
admin.site.register(FeedBack)
