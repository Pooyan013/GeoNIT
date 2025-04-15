from django.db import models
from datetime import datetime

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    units = models.IntegerField()
    days = models.CharField(max_length=50)  # روزها به صورت لیست جدا شده با ویرگول ذخیره می‌شوند.
    start_time = models.TimeField()
    end_time = models.TimeField()
    exam_date = models.DateField()
    exam_time = models.TimeField()

    def __str__(self):
        return self.course_name

    def check_conflict(self, new_days, new_start_time, new_end_time):
        new_start_time = datetime.strptime(str(new_start_time), "%H:%M").time()
        new_end_time = datetime.strptime(str(new_end_time), "%H:%M").time()

        existing_courses = Course.objects.filter(days__in=new_days)
        
        for course in existing_courses:
            if not (new_end_time <= course.start_time or new_start_time >= course.end_time):
                return True  
        return False
