from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewAPI

router = DefaultRouter()
router.register('books', BookViewAPI, basename='books')

urlpatterns = [
    path('', include(router.urls)),
]
