from .models import CustomUser
from rest_framework.response import Response

from rest_framework import status


class CustomUserQuery:
    def __init__(self):
        pass

    @staticmethod
    def getUserByEmail(email:str):
        try:
            obj = CustomUser.objects.filter(email__iexact=email).first()
        except:
            obj = None
        return obj

    @staticmethod
    def getUserByMob(mobile:str):
        try:
            obj = CustomUser.objects.filter(mobile_no=mobile).first()
        except:
            obj = None
        return obj
    @staticmethod
    def getUserByRoleId(roleId:int):
        try:
            objs = CustomUser.objects.filter(id_user_role=roleId).all()
        except:
            objs = None
        return objs

    @staticmethod
    def getUserById(id:int):
        try:
            obj = CustomUser.objects.filter(id=id).first()
        except:
            obj = None
        return obj
    

class Twillio:
    def __init__(self):
        pass
        
    def sendOtp(self,phone,code="+91"):
        print(phone,"<< phone")
        if phone and len(phone) == 10:
            return Response({"message":"OTP SENT"},status=status.HTTP_200_OK)
        else:
            
            return Response({"message":"Invalid Phone"},status=status.HTTP_400_BAD_REQUEST)