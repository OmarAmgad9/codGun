from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)
    confirm_password = serializers.CharField(max_length=100, write_only=True)

    def create(self, validated_data):
        
        
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError({'message': 'Email or password is incorrect'})
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        print(password)
        try:
            user = User(**validated_data)
            user.set_password(password)
            user.save()
        except Exception as e:
            raise serializers.ValidationError({'message': 'Login failed, May be user already exists'})
        return user
        


class ProfileSerializer(serializers.Serializer):
    bio = serializers.CharField(max_length=500, required=False)
    avatar = serializers.ImageField(required=False)
    phone = serializers.CharField(max_length=15, required=False)

    def create(self, validated_data):
        profile = self.objects.create( **validated_data)
        return profile
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    

class GetProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Profile
        fields = ['bio', 'avatar', 'phone']