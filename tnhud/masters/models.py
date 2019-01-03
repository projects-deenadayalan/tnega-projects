from django.db import models

# Create your models here.
 class District(models.Model):
     district_code=models.TextField()
     district_name=models.CharField(max_length=100)
