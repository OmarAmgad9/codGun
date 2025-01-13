from django.urls import path
from . import views

urlpatterns = [
    path('post', views.getAllMyJob, name='post'),
    path('', views.getJobPost, name='job')
]
