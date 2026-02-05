from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from .models import books
from .serializers import Book_Serializer
from .filters import BookFilter

class BookViewAPI(ModelViewSet):
    queryset = books.objects.filter(is_active=True)
    serializer_class = Book_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({
            "success": True,
            "message": "Book added successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    # ✅ SOFT DELETE (THIS IS THE KEY)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()

        return Response({
            "success": True,
            "message": "Book deactivated successfully"
        }, status=status.HTTP_200_OK)
