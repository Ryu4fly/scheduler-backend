from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProfileSerializer

from scheduler.models import Profile
from scheduler.utils import search_profiles

from api import serializers


@api_view(['GET'])
def getRoutes(request):

  routes = [
    {'GET': 'api/profiles'},

    {'GET': 'api/profile/id'},
    {'PUT': 'api/profile/id/update'},
    {'DELETE': 'api/profile/id/delete'},

  ]
  return Response(routes)


@api_view(['GET'])
def get_profiles(request):
  profiles = search_profiles(request)

  serializer = ProfileSerializer(profiles, many=True)

  return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_profile(request,pk):

  try:
    profile = Profile.objects.get(id=pk)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update_profile(request, pk):

  try:
    profile = Profile.objects.get(id=pk)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'PUT':
    serializer = ProfileSerializer(profile, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_profile(request, pk):

  try:
    profile = Profile.objects.get(id=pk)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'DELETE':
    profile.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
