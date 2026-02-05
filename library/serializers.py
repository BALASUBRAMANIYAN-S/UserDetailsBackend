from rest_framework.serializers import ModelSerializer
from .models import books

class Book_Serializer(ModelSerializer):
    class Meta :
        model = books
        fields = "__all__"