from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import JobPost
from .serializers import JobPostSerializer,CreateJobSerializer
from rest_framework.pagination import PageNumberPagination
from account import utils
from . import filter

@api_view(['GET'])
def getAllMyJob(request):
    user_id = utils.getUserId(request)
    job_posts = JobPost.objects.filter(user_id=user_id)
    data, paginator = filter.filterFunction(request, job_posts)
    serializer = JobPostSerializer(data, many=True)
    return paginator.get_paginated_response(serializer.data)
    

@api_view(['GET', 'POST'])
def getJobPost(request):

    if request.method == 'GET':
        data, paginator = filter.filterFunction(request, JobPost.objects.all())
        serializer = JobPostSerializer(data, many=True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        job_data = request.data.copy()
        job_data['user_id'] = utils.getUserId(request)
        jobSerializer = CreateJobSerializer(data=job_data)
        if jobSerializer.is_valid():
            jobSerializer.save()
        return Response( jobSerializer.data,status=status.HTTP_201_CREATED)
    return Response({"message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)


