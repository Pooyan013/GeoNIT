from django.shortcuts import render
from django.http import JsonResponse
from .models import Course
from datetime import datetime
import json

def check_conflict(course_data):
    start_time = datetime.strptime(course_data['start_time'], '%H:%M:%S').time()
    end_time = datetime.strptime(course_data['end_time'], '%H:%M:%S').time()

    conflicts = Course.objects.filter(days=course_data['days'])

    for course in conflicts:
        if (start_time < course.end_time and end_time > course.start_time):
            return True
    return False

def add_course(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            course_data = {
                'course_name': data.get('course_name'),
                'units': data.get('units'),
                'days': data.get('days'),
                'start_time': data.get('start_time'),
                'end_time': data.get('end_time'),
                'exam_date': data.get('exam_date'),
                'exam_time': data.get('exam_time')
            }

            if check_conflict(course_data):
                return JsonResponse({"error": "تداخل زمانی وجود دارد!"}, status=400)

            new_course = Course.objects.create(
                course_name=course_data['course_name'],
                units=course_data['units'],
                days=course_data['days'],
                start_time=datetime.strptime(course_data['start_time'], '%H:%M:%S').time(),
                end_time=datetime.strptime(course_data['end_time'], '%H:%M:%S').time(),
                exam_date=course_data['exam_date'],
                exam_time=course_data['exam_time']
            )

            total_units = Course.objects.aggregate(sum('units'))['units__sum']

            return JsonResponse({
                "course_name": new_course.course_name,
                "units": new_course.units,
                "days": new_course.days,
                "start_time": new_course.start_time.strftime('%H:%M:%S'),
                "end_time": new_course.end_time.strftime('%H:%M:%S'),
                "exam_date": new_course.exam_date,
                "exam_time": new_course.exam_time,
                "total_units": total_units
            }, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return render(request, 'planner/planner.html')
