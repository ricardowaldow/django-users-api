""" URL Paths """
from django.contrib import admin
from django.urls import path, include
from django.db import router
from rest_framework import routers

from users.views import UsersViewSet, user_login

router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='Users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', user_login),
]
