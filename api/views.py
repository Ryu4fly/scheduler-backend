from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProfileSerializer

from scheduler.models import Profile

from api import serializers


@api_view(['GET'])
def getRoutes(request):

  routes = [
    {'GET': 'api/profiles'},
    {'GET': 'api/profile/id'},
  ]
  return Response(routes)

@api_view(['GET'])
def getProfiles(request):
  profiles = Profile.objects.exclude(id='daa4a24d-e912-4ee8-8c93-71dda56488a1')
  serializer = ProfileSerializer(profiles, many=True)

  return Response(serializer.data)

@api_view(['GET'])
def getProfile(request,pk):
  profile = Profile.objects.get(id=pk)
  serializer = ProfileSerializer(profile, many=False)

  return Response(serializer.data)
