from django.urls import path
from . import views

app_name = "universidad"

urlpatterns = [
    path("", views.home, name="home"),

    path("programas/", views.program_list, name="programs"),
    path("programas/<int:id>/", views.program_detail, name="program_detail"),

    path("cursos/", views.course_list, name="courses"),
    path("cursos/<int:id>/", views.course_detail, name="course_detail"),

    path("estudiantes/", views.student_list, name="students"),
    path("estudiantes/<int:id>/", views.student_detail, name="student_detail"),
]