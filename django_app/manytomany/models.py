from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(
        'Student',
    )

    def __str__(self):
        return self.title
