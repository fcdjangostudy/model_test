from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)


class Lecture(models.Model):
    title = models.CharField(max_length=100)
    students = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE,
    )
