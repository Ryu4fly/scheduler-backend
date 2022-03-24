from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
  path('token-login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),

  path('', views.getRoutes),
  path('profiles/', views.getProfiles),
  path('profile/<str:pk>/', views.getProfile)
]
