from rest_framework import routers
from rest_framework.authtoken import views

from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet, 'posts')
router_v1.register('groups', GroupViewSet, 'groups')
router_v1.register(r'posts\/[\d]+\/comments', CommentViewSet, 'comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls))
]
