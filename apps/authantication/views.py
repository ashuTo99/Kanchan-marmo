from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.core.mail import BadHeaderError
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from apps.users.models import CustomUser
from .forms import LoginForm,UserProfileForm
from django.contrib.auth.hashers import make_password
from django.db.models import Q

@csrf_exempt
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'logged in ')
                return redirect("dashboard.index")
            else:
                messages.error(request, 'invalid credentials')
                return redirect("userLogin")
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:

        form = LoginForm()
    context = {
        "form": form
    }
    return render(request , 'base_login.html',context)



@login_required(login_url='userLogin')
def profile(request):
    userObj = CustomUser.objects.filter(id=int(request.user.id)).first()
    if request.method == "POST":
        form = UserProfileForm(request.POST,instance=userObj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successfully')
            return redirect("dashboard.index")
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = UserProfileForm(instance=userObj)

    context = {
        "form": form,
        "data":userObj
    }
    return render(request,"profile.html",context)


@login_required(login_url='userLogin')
def userLogout(request):
    logout(request)
    messages.success(request, 'logged out !')
    return redirect("userLogin")
