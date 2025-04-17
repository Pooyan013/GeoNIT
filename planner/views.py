from django.shortcuts import render
from django.http import JsonResponse
from .models import Course, Schedule
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Course
from django.template.loader import get_template
import pdfkit
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def add_course(request):
    if request.method == "POST":
        # دریافت داده‌ها از فرم
        course_name = request.POST.get("course_name")
        units = int(request.POST.get("units"))
        exam_date = request.POST.get("exam_date")
        exam_time = request.POST.get("exam_time")
        
        days = [request.POST.get(f"day{i}") for i in range(units)]
        times = [request.POST.get(f"time{i}") for i in range(units)]
        
        for day, time in zip(days, times):
            existing_schedules = Schedule.objects.filter(day=day, time=time)
            if existing_schedules.exists():
                return JsonResponse({"error": f"تداخل زمانی برای کلاس {course_name} در روز {day} و ساعت {time} وجود دارد."}, status=400)

        course = Course(course_name=course_name, units=units, exam_date=exam_date, exam_time=exam_time)
        course.save()

        for day, time in zip(days, times):
            if day and time:  
                course.schedule.create(day=day, time=time)

        return JsonResponse({
            "course_name": course_name,
            "units": units,
            "exam_date": exam_date,
            "exam_time": exam_time,
            "days": days,
            "times": times
        })

    return render(request, 'planner/planner.html')


@csrf_exempt
def delete_course(request):
    if request.method == "POST":
        course_name = request.POST.get("course_name")
        course = get_object_or_404(Course, course_name=course_name)
        course.delete()
        return JsonResponse({"status": "success"})

def export_pdf(request):
    courses = Course.objects.prefetch_related("schedule").all()
    template = get_template("planner/pdf_template.html")
    html = template.render({"courses": courses})
    pdf = pdfkit.from_string(html, False)
    return HttpResponse(pdf, content_type='application/pdf')
