from django.db import models

# Create your models here.

class task(models.Model):
    task_name = models.CharField('Task Name', max_length=20)