from django.db import models

class Lesson(models.Model):
    name = models.CharField(max_length=200)
    unit = models.IntegerField()
    day = models.CharField(max_length=10)  # Monday, Tuesday, etc.
    time = models.CharField(max_length=10)  # Time format: HH:MM
    exam_day = models.CharField(max_length=10)  # Day of the exam
    exam_time = models.CharField(max_length=10)  # Time of the exam

    def __str__(self):
        return self.name