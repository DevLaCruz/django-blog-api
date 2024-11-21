from rest_framework.routers import DefaultRouter
from .views import CommentApiViewSet


router_commets=DefaultRouter()

router_commets.register(prefix='comments', basename='comments', viewset=CommentApiViewSet)