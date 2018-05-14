from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "courses_app/index.html")
