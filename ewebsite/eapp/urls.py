from django.urls import path
from django.contrib.auth import views as auth_view
from eapp import views
from django.conf import settings
from django.conf.urls import static
app_name='eapp'
urlpatterns=[
   path('login/',auth_view.LoginView.as_view(template_name='eapp/login.html'),name='login'),
   path('logout/',auth_view.LogoutView.as_view(),name='logout'),
   path('signup/',views.SignUp.as_view(),name='signup'),
   path('category/',views.CreateCategory.as_view(),name='category'),
   path('product/<int:pk>/',views.ProductDetail.as_view(),name='detail'),
   path('confirm/',views.ConfirmEmail,name='confirm_email'),
   path('check/',views.CheckCode,name='check'),
   path('placed/',views.Thanks,name='placed'),
   path('trythis/',views.tryThis,name='trythis'),
   path('createproduct/',views.CreateProduct.as_view(),name='create_product'),
   path('feedback/',views.CreateFeedBack.as_view(),name='feedback'),
   path('feedback_reveive/',views.FeedbackReceive.as_view(),name='feedback_reveive')
]
