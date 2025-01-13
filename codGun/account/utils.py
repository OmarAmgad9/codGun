from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from . import models


def getUserId(request):
    
    token = request.headers.get('Authorization')
    try:
        user = Token.objects.get(key=token[6:])
        return user.user_id
    except:
        return Response({'message': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

def getUserProfile(user_id):
    try:
        profile = models.Profile.objects.get(user_id=user_id)
        return profile
    except:
        return Response({'message': 'User Not Valid'}, status=status.HTTP_401_UNAUTHORIZED)

