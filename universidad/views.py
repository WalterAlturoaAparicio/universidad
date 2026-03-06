from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "universidad/home.html", {})

def student_list(request):
    return render(request, "universidad/home.html", {})

def program_list(request):
    return render(request, "universidad/home.html", {})

def course_list(request):
    return render(request, "universidad/home.html", {})
