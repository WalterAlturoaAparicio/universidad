from django.shortcuts import render, get_object_or_404
from .models import Program, Course, Student


def home(request):
    return render(request, "universidad/home.html")


# LISTAS

def program_list(request):
    programs = Program.objects.all()
    return render(request, "universidad/program_list.html", {
        "programs": programs
    })


def course_list(request):
    courses = Course.objects.select_related("program").all()
    return render(request, "universidad/course_list.html", {
        "courses": courses
    })


def student_list(request):
    students = Student.objects.all()
    return render(request, "universidad/student_list.html", {
        "students": students
    })


# DETALLES

def program_detail(request, id):
    program = get_object_or_404(Program, id=id)
    return render(request, "universidad/program_detail.html", {
        "program": program
    })


def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, "universidad/course_detail.html", {
        "course": course
    })


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, "universidad/student_detail.html", {
        "student": student
    })