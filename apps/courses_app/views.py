from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course

def index(request):
    return render(request, "courses_app/index.html", {"courses":Course.objects.all().values()})

def new(request):
    # capture data
    name = request.POST["name"]
    description = request.POST["description"]
    # validate data (name > 5 and desc > 15)
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for value in errors.values():
            messages.error(request, value)
        return redirect("/")
    else:
        # insert data
        Course.objects.create(name=name,description=description)
        messages.success(request, "Course created successfully!")
        # redirect back to home page
        return redirect("/")

    

def confirm(request,course_id):
    print("confirm page:", course_id)
    course = {"course_id": course_id}
    return render(request, "courses_app/confirm.html",course)

def destroy(request, course_id):
    print('destroy has been confimed: ', course_id)
    return redirect("/")
