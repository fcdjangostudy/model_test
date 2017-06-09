from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @property
    def find_room(self):
        return [i.classroom.class_room_number for i in self.manytomany_lecture.all()]



class Lecture(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(
        'Student',
        through='Enrollment',
        related_name='%(app_label)s_%(class)s',
    )

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    lecture = models.ForeignKey(Lecture)
    student = models.ForeignKey(Student)
    enrollment_date = models.DateField(auto_now_add=True)

    # class Meta:
    #     db_table = 'manytomany_lecture_students'


class ClassRoom(models.Model):
    class_room_number = models.PositiveIntegerField(default=701, blank=True, null=True)
    lecture = models.OneToOneField(
        'Lecture',
        on_delete=models.CASCADE,
    )
