from rest_framework.views import APIView
from rest_framework.response import Response
from Serializer import RegisterSerializer

class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"})
        return Response(serializer.errors, status=400)
