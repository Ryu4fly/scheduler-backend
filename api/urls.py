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
  path('profiles/', views.get_profiles),
  path('profile/<str:pk>/', views.get_profile),
  path('profile/<str:pk>/update/', views.update_profile),
  path('profile/<str:pk>/delete/', views.delete_profile)
]
