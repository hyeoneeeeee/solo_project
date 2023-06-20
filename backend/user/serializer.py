from rest_framework import serializers
from user.models import UserModel
import re
from user.validators import PasswordValidator



class SignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=50, write_only=True)

    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs['password2']
        PasswordValidator.validate(password, password2)
        return super().validate(attrs)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.username = validated_data["username"]
        user.set_password(validated_data["password"])
        user.is_active = True
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = "__all__"

