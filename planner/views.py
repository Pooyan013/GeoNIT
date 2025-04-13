from django.shortcuts import render
from django.http import JsonResponse
from .forms import LessonForm
from .models import Lesson

def check_conflict(day, time):
    conflicts = Lesson.objects.filter(day=day, time=time)
    return conflicts.exists()

def planner_view(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            day = form.cleaned_data['day']
            time = form.cleaned_data['time']
            if check_conflict(day, time):
                return JsonResponse({'error': 'تداخل زمانی وجود دارد.'})

            form.save()
            lessons = Lesson.objects.all()
            return render(request, 'planner/planner.html', {'form': form, 'lessons': lessons, 'success': True})
    else:
        form = LessonForm()
        lessons = Lesson.objects.all()

    return render(request, 'planner/planner.html', {'form': form, 'lessons': lessons})