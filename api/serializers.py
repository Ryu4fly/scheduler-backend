from rest_framework import serializers

from scheduler.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    exclude = [ 'user' ]
