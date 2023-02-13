from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting

# Create your views here.

def welcome(request):
    return render(request, "mywebsite/welcome.html",
                  {"meetings": Meeting.objects.all()})

def welcome_date(request):
    return HttpResponse("Hey there. You are really welcome here!!... " + str(datetime.now()))

def about(request):
    return HttpResponse("Hey there. You are really welcome here!!... " + str(datetime.now()))
