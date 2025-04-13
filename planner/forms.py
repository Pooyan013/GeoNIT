from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'unit', 'day', 'time', 'exam_day', 'exam_time']