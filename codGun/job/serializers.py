from  . import models
from rest_framework import serializers
from category.serializer import SkillsSerializer, JobAddSkillsSerializer
from category.models import Skills
from category.models import Category, Skills



class JobPostSerializer(serializers.ModelSerializer):
    skills = SkillsSerializer(many=True, read_only=True) 
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = models.JobPost
        fields =  ['title', 'description', 'min_budget', 'max_budget', 'category', 'skills']




from rest_framework import serializers
class skillPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model: models.Skills
        fields = ['name']


class CreateJobSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=5000)
    min_budget = serializers.DecimalField(max_digits=10, decimal_places=2)
    max_budget = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = serializers.CharField()
    skills = serializers.ListSerializer(
        child=serializers.CharField(max_length=50),
        required=False, 
        allow_empty=True,
    )
    user_id = serializers.CharField(max_length=20, write_only=True)

    def create(self, validated_data):
        skills_data = validated_data.pop('skills', [])
        cate = validated_data.pop('category', [])        
        category =Category.objects.get(name=cate)
        try:

            job = models.JobPost.objects.create(category=category , **validated_data)
            for skill in skills_data:

                arr, created = Skills.objects.get_or_create(name= skill)
                if not arr:
                    job.skills.add(created)
                else: 
                    job.skills.add(arr)

        except Exception as e:
            print(e)
            raise serializers.ValidationError("Invalid data")
        return job

