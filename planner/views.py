from django.shortcuts import render
from django.http import JsonResponse
from .models import Course, Schedule

def add_course(request):
    if request.method == "POST":
        # دریافت داده‌ها از فرم
        course_name = request.POST.get("course_name")
        units = int(request.POST.get("units"))
        exam_date = request.POST.get("exam_date")
        exam_time = request.POST.get("exam_time")
        
        # دریافت روزها و ساعات
        days = [request.POST.get(f"day{i}") for i in range(units)]
        times = [request.POST.get(f"time{i}") for i in range(units)]
        
        # ذخیره درس جدید
        course = Course(course_name=course_name, units=units, exam_date=exam_date, exam_time=exam_time)
        course.save()
      
        for day, time in zip(days, times):
            course.schedule.create(day=day, time=time)

        # ارسال پاسخ JSON با داده‌های درس جدید
        return JsonResponse({
            "course_name": course_name,
            "units": units,
            "exam_date": exam_date,
            "exam_time": exam_time,
            "days": days,
            "times": times
        })

    return render(request, 'planner/planner.html')
