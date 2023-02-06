from django.db import models

class Post(models.Model):
    name=models.CharField(max_length=80)
    address=models.CharField(max_length=90)
    subject=models.CharField(max_length=90)

    
