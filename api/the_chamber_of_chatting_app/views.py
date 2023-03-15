from django.contrib.auth.models import User

from rest_framework import viewsets



from .models import Topic, Message
from .serializers import TopicSerializer, MessageSerializer, UserSerializer
# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class TopicViewSet(viewsets.ModelViewSet):
    """API endpoint that allows topics to be viewed or edited."""
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer