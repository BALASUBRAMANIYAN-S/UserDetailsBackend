from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentTask
from .serializers import Task_serializer, User_serializer

class TaskViewAPI(APIView):
    def post (self,request):
        new_task = Task_serializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            return Response(data=new_task.data)
        else:
            return Response(new_task.errors)

    def get (self,request):
        all_task = StudentTask.objects.all()
        task_data = Task_serializer(all_task, many=True)
        return Response(task_data.data)

class UserViewAPI(APIView):
    def post (sel,request):
        get_user = User_serializer(data=request.data)
        if get_user.is_valid():
            get_user.save()
            return Response(data=get_user.data)
        else:
            return Response(get_user.errors)

class TaskViewUpdateAPI(APIView):
    def put (self, request, task_id):

        task = StudentTask.objects.as_view()
        