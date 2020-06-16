from django.shortcuts import render,get_list_or_404,HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy,reverse
from eapp import forms
from django.views.generic import TemplateView,CreateView,DeleteView,ListView,DetailView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from eapp.models import Category,EmailVerified,User,Order,Product
from eapp import models
import random
from django.core.mail import send_mail
# Create your views here.
class Index(ListView):
    template_name='eapp/parallax.html'
    model=models.Category
    context_object_name='category_list'
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name='eapp/signup.html'
    success_url=reverse_lazy('login')
class CreateCategory(CreateView,LoginRequiredMixin):
    login_url='eapp:login'
    model=models.Category
    template_name='eapp/createcategory.html'
    fields=('product_category',)
    success_url=reverse_lazy('home')
class CreateProduct(LoginRequiredMixin,CreateView):
    login_url='eapp:login'
    model=models.Product
    template_name='eapp/createproduct.html'
    fields=('name','category','price','photo','discription','color')
    success_url=reverse_lazy('eapp:create_product')
class ProductList(ListView):
    template_name='eapp/productlist.html'
    model=Product
    def get_queryset(self):
        qs=super(ProductList,self).get_queryset()
        return qs.filter(category__exact=self.kwargs['cat'])
class ProductDetail(DetailView):
    model=models.Product
    context_object_name='product_detail'
    template_name='eapp/detail.html'
class CreateOrder(LoginRequiredMixin,CreateView):
        login_url='eapp:login'
        model=models.Order
        template_name='eapp/order.html'
        fields=('quantity','phone','pincode','Address')
        def form_valid(self,form):
            form.instance.user=self.request.user
            form.instance.product_id=self.kwargs['id']
            return super(CreateOrder,self).form_valid(form)
        success_url=reverse_lazy('eapp:placed')
def Thanks(request):

    us=EmailVerified.objects.get(user=request.user)
    name=us.user.username
    #p=Order.objects.filter(user=request.user)
    #pname=p.product.name
    #price=p.product.price
    context={'name':name,'email':us.user.email}
    send_mail(
     'Successful Order',
     'Dear {},You have succesfully placed order ,we will ensure fastest delivery and best product quality from our side.Thank you....'.format(name),
     'bathlaofficial@gmail.com',
     [us.user.email],
     fail_silently=False)
    return render(request,'eapp/order_thanks.html',context)


    #    form.instance.product

def ConfirmEmail(request):

    us= EmailVerified.objects.get(user=request.user)
    if us.status=='pending':
        us=EmailVerified.objects.get(user=request.user)
        email=us.user.email
        stat=us.status
        context={'email':email}
        send_mail(
         'Welcome to E-Mart',
         'Confirm your email by Verification code {} ,you are receiving this email as you wants email verfication with us ,please ignore if do not apply.Enjoy amazing offers'.format(us.unique_number),
         'bathlaofficial@gmail.com',
         [us.user.email],
         fail_silently=False)
        return render(request,'eapp/confirm_email.html',context)

    else: return render(request,'eapp/parallax.html')


def tryThis(request):
    try:
        ikd=request.user.id
        code=random.randrange(100000,999999)
        ad=EmailVerified.objects.create(user_id=ikd,unique_number=code)
        ad.save()

    finally:
        return HttpResponseRedirect(reverse('eapp:confirm_email'))
def CheckCode(request):
    if request.method=="POST":
        usercode=request.POST.get('code')
        us=EmailVerified.objects.get(user=request.user)
        code=us.unique_number
        if int(usercode) == int(code):
            us.status='confirmed'
            us.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid code,please go back and re-enter correct code ')
    else:return render(request,'eapp/confirm_email.html')
class CreateFeedBack(LoginRequiredMixin,CreateView):
    login_url='eapp:login'
    model=models.FeedBack
    fields=('feedback',)
    template_name='eapp/feedback.html'
    success_url=reverse_lazy('eapp:feedback_reveive')
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(CreateFeedBack,self).form_valid(form)
class FeedbackReceive(TemplateView):
    template_name='eapp/tq.html'
