from django.db.models import Q

from .models import Profile


def search_profiles(request):
  search_query = ''

  if request.data:
    search_query = request.data['search_query']

  profiles = Profile.objects.distinct().filter(
      Q(username__icontains=search_query) |
      Q(email__icontains=search_query) |
      Q(first_name__icontains=search_query) |
      Q(last_name__icontains=search_query)
  )

  return profiles
