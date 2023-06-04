from django.urls import path
from .import views


urlpatterns = [
    path("login/",views.login,name="userLogin"),
    path("profile/",views.profile,name="profile"),

    path('logout/' , views.userLogout , name='userlogout' ),

]
