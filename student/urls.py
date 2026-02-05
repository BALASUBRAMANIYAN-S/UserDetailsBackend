from django.urls import path
from .views import TaskViewAPI,UserViewAPI

urlpatterns = [
   path('task/', TaskViewAPI.as_view()),
   path('user/', UserViewAPI.as_view()),
]
