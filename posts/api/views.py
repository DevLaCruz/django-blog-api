from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from .serializers import PostSerializer
from .permissions import IsAdminOrReadonly
from django_filters.rest_framework import DjangoFilterBackend

class PostApiViewSet(ModelViewSet):
    permission_classes=[IsAdminOrReadonly]
    serializer_class=PostSerializer
    #queryset=Category.objects.all()
    queryset=Post.objects.filter(published=True)
    lookup_field='slug'
    filter_backends=[DjangoFilterBackend]
    #filterset_fields=['category']
    filterset_fields=['category','category__slug']
