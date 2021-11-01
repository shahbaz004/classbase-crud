from django.db import models


class Student(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    roll = models.CharField("Roll No", max_length=3)
    mobile = models.CharField(max_length=11)
    program = models.CharField(max_length=10)

