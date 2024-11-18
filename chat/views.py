from rest_framework import viewsets, permissions
from .models import CustomUser, Channel, Message
from .serializers import UserSerializer, ChannelSerializer, MessageSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

def get_queryset(self):
    channel = self.kwargs['channel_id']
    return Message.objects.filter(channel__id=channel)
