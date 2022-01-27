from django.db import models
from django.utils import timezone


class Student(models.Model):
    name = models.CharField(max_length=40)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    create_at = models.DateTimeField(editable=False, default=timezone.now)
