from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductImageView.as_view(), name='index'),
    path('home/', ProductImageView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('products/', products, name='products'),
    path("register/", register, name="register"),
    path("login/", login_request, name="login"),
    path('single/', single, name='single'),
    path("logout", logout_request, name= "logout"),
]
