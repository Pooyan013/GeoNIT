from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    units = models.IntegerField()
    exam_date = models.DateField()
    exam_time = models.TimeField()

    def __str__(self):
        return self.course_name

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='schedule')
    day = models.CharField(max_length=10)
    time = models.CharField(max_length=5)
    
    def __str__(self):
        return f"{self.day} - {self.time}"
