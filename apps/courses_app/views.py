from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "courses_app/index.html")

def new(request):
    # capture data
    name = request.POST["name"]
    description = request.POST["description"]
    # validate data (name > 5 and desc > 15)

    # insert data

    # redirect back to home page
    print("just added a new course")
    return redirect("/")

def confirm(request,course_id):
    print("confirm page:", course_id)
    course = {"course_id": course_id}
    return render(request, "courses_app/confirm.html",course)

def destroy(request, course_id):
    print('destroy has been confimed: ', course_id)
    return redirect("/")
