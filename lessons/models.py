from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    time = models.CharField(max_length = 50, blank=True)
    location = models.ManyToManyField('Location', blank=True)
    grade = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
