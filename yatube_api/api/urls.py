from rest_framework import routers
from rest_framework.authtoken import views

from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, PostViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts\/[\d]+\/comments', CommentViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls))
]
