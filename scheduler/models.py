from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  location = models.CharField(max_length=250)
  gamer_profiles = {
    'steam': '',
    'ea': '',
    'blizzard': '',
    'rockstar': '',
  }
  friends = models.ManyToManyField('Profile')

class friend_status(models.Model):
  status = {
    'pending': 0,
    'accepted': 1
  }
  inviting_user = models.ForeignKey(Profile, related_name="inviting_user")
  accepting_user = models.ForeignKey(Profile, related_name="accepting_user")

class Group(models.Model):
  name = models.CharField(max_length=250)
  users = models.ManyToManyField(Profile)

class Timezone(models.Model):
  name = models.CharField(max_length=50)

class TimeSlot(models.Model):
  schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
  start_date = models.DateTimeField()
  end_date = models.DateField()


class Schedule(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  timezones = models.ManyToManyField(Timezone)
