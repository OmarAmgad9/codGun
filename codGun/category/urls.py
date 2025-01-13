from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.getCategory, name='category'),
    path('skills', views.getSkills, name='skills'),
]

