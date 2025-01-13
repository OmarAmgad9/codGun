from django.db import models
from category.models import Category, Skills
from django.contrib.auth.models import User

class JobPost(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=5000,blank=False, null=False)
    min_budget = models.DecimalField(max_digits=10,  decimal_places=2)
    max_budget = models.DecimalField(max_digits=10,  decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills, related_name='jobs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
