from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required(login_url='userLogin')
def index(request):
    userObjs = CustomUser.objects.filter(is_admin=False,is_deleted=False)

    context = {
        "results":userObjs,
    }
    return render(request,"users/index.html",context)
