from django.urls import path, include
from .views import LoginView, LogoutView, UserModelViewSet, GroupModelViewSet#, SignupView
# Django REST Framework
from rest_framework.routers import DefaultRouter # type: ignore

router = DefaultRouter()

router.register(r'users', UserModelViewSet, basename='users')
router.register(r'group', GroupModelViewSet, basename='group')

urlpatterns = [
# Auth views
     path('auth/login/',  LoginView.as_view(), name='auth_login'),
     path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
     # path('auth/signup/', SignupView.as_view(), name='auth_signup'),
     path('', include(router.urls)),
     path('auth/reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]