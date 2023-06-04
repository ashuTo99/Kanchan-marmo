from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.hashers import check_password
from apps.users.models import CustomUser

class LoginForm(forms.Form):
    email = forms.CharField(
        required=True,
        label='Your Email',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-user",
                   'placeholder': 'Email'}),
        error_messages={
            'required': 'Email is required'
        }
    )
    password = forms.CharField(
        required=True,
        label='Your Password',
        widget=forms.PasswordInput(
            attrs={'class': "form-control form-control-user",
                   'placeholder': 'Password'}),
        error_messages={
            'required': 'Password is required'
        }
    )

    def clean_email(self):
        data = self.cleaned_data
        email = data.get('email')
        if email == "" or email is None:
            raise ValidationError(self.fields['email'].error_messages['required'])
        return email

    def clean_password(self):
        data = self.cleaned_data
        password = data.get('password')
        if password == "" or password is None:
            raise ValidationError(self.fields['password'].error_messages['required'])
        return password


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        label='First Name',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Category Name'}),
        error_messages={
            'required': 'First name is required'
        }
    )
    last_name = forms.CharField(
        required=True,
        label='Last Name',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Category Name'}),
        error_messages={
            'required': 'Last name is required'
        }
    )
    email = forms.CharField(
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs={'class': "form-control ",
                   'placeholder': 'Category Name'}),
        error_messages={
            'required': 'Email is required'
        }
    )
    mobile_no = forms.CharField(
        required=True,
        label='Mobile',
        widget=forms.TextInput(
            attrs={'class': "form-control ",
                   'placeholder': ''}),
        error_messages={
            'required': 'Mobile field  is required'
        }
    )
    class Meta:
        model = CustomUser
        fields= ['first_name','last_name','email','mobile_no']

    def clean_first_name(self):
        data = self.cleaned_data
        first_name = data.get('first_name')
        if first_name == "" or first_name is None:
            raise ValidationError(self.fields['first_name'].error_messages['required'])
        return first_name
    
    def clean_last_name(self):
        data = self.cleaned_data
        last_name = data.get('last_name')
        if last_name == "" or last_name is None:
            raise ValidationError(self.fields['last_name'].error_messages['required'])
        return last_name
    
    def clean_email(self):
        data = self.cleaned_data
        email = data.get('email')
        if email == "" or email is None:
            raise ValidationError(self.fields['email'].error_messages['required'])
        return email
    
    def clean_mobile_no(self):
        data = self.cleaned_data
        mobile_no = data.get('mobile_no')
        if mobile_no == "" or mobile_no is None:
            raise ValidationError(self.fields['mobile_no'].error_messages['required'])
        return mobile_no