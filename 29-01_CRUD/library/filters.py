from django_filters import rest_framework as filters
from .models import books

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    class Meta :
        Model = books
        fields = [
            'title',
        ]
