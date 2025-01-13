from rest_framework.response import Response

from .serializer import CategorySerializer,SkillsSerializer
from . import models
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def getCategory(request):
    
    if request.method == 'GET':
        cat = request.GET.get('cat')
        limit = request.GET.get('limit')
        sort = request.GET.get('sort')
        print(limit)
        print(type(limit))
        print(sort)
        if not sort: 
            sort = 'name'
        if limit:
            limit = int(limit)
        if cat:
            cat = cat.split(',')
            print(sort)
            category = models.Category.objects.filter(name__in=cat)[:limit].order_by(sort)
        else:
            category = models.Category.objects.all().order_by(sort)[:limit]

        if category:
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    return Response({'message': 'Not Found'},status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getSkills(request):
    cat = request.GET.get('cat')
    limit = 10
    limit = request.GET.get('limit')
    if not limit:
        limit = 10
    if cat:
        skills = models.Skills.objects.filter(Category__name=cat)[:int(limit)]
    else:
        skills = models.Skills.objects.all()[:int(limit)]
        
    
    serializer = SkillsSerializer(skills, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    


