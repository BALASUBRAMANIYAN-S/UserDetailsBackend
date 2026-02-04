from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewAPI

router = DefaultRouter()
router.register('BookViewAPI', BookViewAPI, basename='BookViewAPI')
urlpatterns = [
    path('',include(router.urls))
] 