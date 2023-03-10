from django.contrib.auth.models import User

from rest_framework import viewsets



from .models import Topic, Message
from .serializers import TopicSerializer, MessageSerializer, UserSerializer
# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer