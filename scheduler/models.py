from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  username = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  location = models.CharField(max_length=250)
  gamer_profiles = {
    'steam': '',
    'ea': '',
    'blizzard': '',
    'rockstar': '',
  }
  friends = models.ManyToManyField('Profile')

  def __str__(self):
    return self.username
class friend_status(models.Model):
  status = {
    'pending': 0,
    'accepted': 1
  }
  inviting_user = models.ForeignKey(Profile, related_name="inviting_user", on_delete=models.CASCADE)
  accepting_user = models.ForeignKey(Profile, related_name="accepting_user", on_delete=models.CASCADE)

class Group(models.Model):
  name = models.CharField(max_length=250)
  users = models.ManyToManyField(Profile)

class Timezone(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class TimeSlot(models.Model):
  schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
  start_date = models.DateTimeField()
  end_date = models.DateField()

class Schedule(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  timezones = models.ManyToManyField(Timezone)
