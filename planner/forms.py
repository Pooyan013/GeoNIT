from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'units', 'days', 'start_time', 'end_time', 'exam_date', 'exam_time']

    class Media:
        js = ('planner/js/course_form.js',)
