import uuid
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  username = models.CharField(max_length=100)
  email = models.EmailField()
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  location = models.CharField(max_length=250)
  gamer_profiles = models.JSONField(default=dict)
  friends = models.ManyToManyField('Profile')

  def __str__(self):
    return self.username

class friend_status(models.Model):
  STATUS_TYPE = {
    ('PENDING', 'Pending'),
    ('ACCEPTED', 'Accept'),
    ('IGNORED', 'Ignore')
  }
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
  inviting_user = models.ForeignKey(Profile, related_name="inviting_user", on_delete=models.CASCADE)
  accepting_user = models.ForeignKey(Profile, related_name="accepting_user", on_delete=models.CASCADE)
  status = models.CharField(max_length=20, default='PENDING', editable=False)


class Group(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
  name = models.CharField(max_length=250)
  users = models.ManyToManyField(Profile)

  def __str__(self):
    return self.name


class Timezone(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


class TimeSlot(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
  schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
  start_date = models.DateTimeField()
  end_date = models.DateField()


class Schedule(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  timezones = models.ManyToManyField(Timezone)
