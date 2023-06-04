from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from apps.users.query import CustomUserQuery
from apps.api.query import generateOTP,generateUidString



class UserRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    mobile_no = serializers.CharField(required=True)
    user_role_id = serializers.IntegerField(required=True)

    def validate(self,data):
        email = data.get('email','')
        mobile_no = data.get('mobile_no','')
        password = data.get('password','') 
        confirm_password = data.get('confirm_password','') 

        if email:
            obj = CustomUserQuery.getUserByEmail(email)
            if obj:
                serializers.ValidationError("Account with this email is already exists")
        else:
            raise serializers.ValidationError("Email field is required")

        if mobile_no:
            obj = CustomUserQuery.getUserByMob(mobile_no)
            if obj:
                raise serializers.ValidationError("Account with this mobile number is already exists")
        else:
            raise serializers.ValidationError("Mobile number field is required")
        
        if password and confirm_password:
            if password  != confirm_password:
                raise serializers.ValidationError("Password and confirm password must be same")
        return data

    def create(self, validated_data):
        email = validated_data.get('email','')
        first_name = validated_data.get('first_name','')
        last_name = validated_data.get('last_name','')
        password = validated_data.get('password','')
        confirm_password = validated_data.get('confirm_password','')
        mobile_no = validated_data.get('mobile_no','')
        user_role_id = validated_data.get('user_role_id',0)

        try:
            user = CustomUser()
            user.email = email
            user.password = make_password(password)
            user.confirm_password = make_password(confirm_password)
            user.mobile_no = mobile_no
            user.first_name = first_name
            user.last_name = last_name
            user.id_user_role = user_role_id
            user.uid_otp = generateOTP(6)
            user.uid_string = generateUidString()
            user.save()
            status = {'uid_string':user.uid_string,'uid_otp':user.uid_otp}
        except Exception as e:
            print(" Exception in create user ===>",e)
            status = {}
        return status