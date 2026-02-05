from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('student.urls')),
    path('students/',include('basicCRUD.urls')),
    path('library/',include('library.urls')), 
]