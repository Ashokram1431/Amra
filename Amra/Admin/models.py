from django.db import models

# Create your models here.
class amra_user(models.Model):
    username=models.TextField(max_length=10)
    password=models.TextField(max_length=10)