from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ChannelViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'channels', ChannelViewSet)
router.register(r'channels/(?P<channel_id>\d+)/messages', MessageViewSet, basename='channel-messages')

urlpatterns = [
path('', include(router.urls)),
]  
