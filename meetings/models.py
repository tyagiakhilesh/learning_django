from datetime import  time
from django.db import models

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title} at {self.date} {self.start_time} for {self.duration}"

class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_number = models.PositiveSmallIntegerField()
    room_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Room name {self.name} on floor {self.floor_number} with number {self.room_number}"
