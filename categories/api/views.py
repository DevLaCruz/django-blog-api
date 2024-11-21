from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminOrReadonly

class CategoryApiViewSet(ModelViewSet):
    permission_classes=[IsAdminOrReadonly]
    serializer_class=CategorySerializer
    #queryset=Category.objects.all()
    queryset=Category.objects.filter(published=True)
    lookup_field='slug'
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['published','title']

