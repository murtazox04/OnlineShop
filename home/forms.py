from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

# class NewUserForm(UserCreationForm):
#     first_name = forms.CharField(max_length=20)
#     last_name = forms.CharField(max_length=20)
#     email = forms.EmailField(required=True)
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)
#     mobile = forms.CharField(max_length=20)

#     class Meta:
#         model = User
#         fields = ("first_name", "last_name", "username", "email", "password1", "password2", "mobile")

#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.first_name = self.first_name
#         user.last_name = self.last_name
#         user.username = self.username
#         user.email = self.email
#         user.password = self.password1
#         user.mobile = self.mobile
#         if commit:
#             user.save()
#         return user

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    # captcha = CaptchaField(label='Enter the code here')
    
    class Meta:
        model = User
        fields = ['username', 'email','phone_no','password1', 'password2']
