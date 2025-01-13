from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializer import UserSerializer, ProfileSerializer, GetProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from . import models
from . import utils

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user_id = utils.getUserId(request)
    profile = utils.getUserProfile(user_id)

    if request.method == 'GET':
        serializer = GetProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':

        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login(request):
    
    phone  = request.data.get('phone')
    email = request.data.get('email')
    
    password = request.data.get('password')

    return Response({'message': "NOTHING FOR Nothing", 
                        'username': phone,
                        'email': email, 
                        'password': password})


