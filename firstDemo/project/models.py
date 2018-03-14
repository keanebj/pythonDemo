from django.db import models  
  
# Create your models here.  
class Stu(models.Model):  
    id = models.CharField(max_length=16,primary_key=True)  
    name=models.CharField(default='dqd',max_length=16)  