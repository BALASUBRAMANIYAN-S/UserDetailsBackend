from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField, IntegerField
from .models import StudentTask,StudentData


class Task_serializer(ModelSerializer):
    details = SerializerMethodField()
    name = CharField(source='student.name', read_only=True)
    age = IntegerField(source='student.age', read_only=True)
    class Meta :
        model = StudentTask
        fields = '__all__'

    def get_details(self, obj):
        return f'{obj.task} {obj.description}'
    
class User_serializer(ModelSerializer):

    class Meta :
        model = StudentData
        fields = '__all__'