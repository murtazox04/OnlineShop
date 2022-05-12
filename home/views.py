from django.shortcuts import render, redirect
from django.views.generic import ListView
# from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from home.models import Product


# Create your views here.

class ProductImageView(ListView):
    model = Product
    template_name = 'blog/index.html'
    context_object_name = 'products'


def contact(request):
    return render(request, 'blog/contact.html')


def products(request):
    return render(request, 'blog/products.html')


def single(request):
    return render(request, 'blog/single.html')


# def register_request(request):
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.succsess(request, 'Account created successfully')
#             return redirect('home:index')
#         messages.error(request, 'Please correct the error below')
#     form = NewUserForm()
#     return render(request, 'blog/register.html', {'register_form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="blog/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home:index")
