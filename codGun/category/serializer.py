from rest_framework import serializers

from .models import Category, Skills

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'image']


class SkillsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='Category.name', read_only=True)
    class Meta:
        model = Skills
        fields =   ['name', 'category_name']
        


class JobAddSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields =   ['name']
