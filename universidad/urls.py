from django.urls import path
from . import views

app_name = "universidad"

urlpatterns = [
    path("", views.home, name="home"),
    path("programas/", views.program_list, name="programs"),
    path("estudiantes/", views.student_list, name="students"),
    path("cursos/", views.course_list, name="courses"),
]

