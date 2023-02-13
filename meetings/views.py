from django.shortcuts import render, get_object_or_404
from .models import Meeting, Room
from django.forms import modelform_factory


def details(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meetingObj": meeting})


def all_rooms(request):
    rooms = Room.objects.all();
    return render(request, "meetings/rooms.html", {"rooms": rooms})


MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
