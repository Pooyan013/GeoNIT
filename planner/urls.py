from django.urls import path
from . import views

urlpatterns = [
    path("add-course/", views.add_course, name="add_course"),
    path("delete/", views.delete_course, name="delete_course"),
    path('export-pdf/', views.export_pdf, name='export_pdf'),
]
