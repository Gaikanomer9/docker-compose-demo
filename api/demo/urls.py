
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (NoteViewSet)

v1_router = DefaultRouter()

v1_router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
