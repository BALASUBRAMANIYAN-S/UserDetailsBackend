from rest_framework.views import APIView
from rest_framework.response import Response
from .models import student 

class StudentAPI(APIView):

    # GET – Read
    def get(self, request):
        students = student.objects.all()
        data = []

        for s in students:
            data.append({
                "Exam": s.Exam,
                "RollNumber": s.RollNumber,
            })

        return Response(data)

    # POST – Create
    def post(self, request):
        exam = request.data.get("Exam")
        roll_number = request.data.get("RollNumber")

        if not exam or not roll_number:
            return Response(
                {"error": "Exam and RollNumber are required"},
                status=400
            )

        new_student = student.objects.create(
            Exam=exam,
            RollNumber=roll_number
        )

        return Response({
            "Exam": new_student.Exam,
            "RollNumber": new_student.RollNumber
        }, status=201)
