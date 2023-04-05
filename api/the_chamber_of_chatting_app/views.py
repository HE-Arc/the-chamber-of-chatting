from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Message, Topic
from .serializers import MessageSerializer, TopicSerializer, UserSerializer

# Create your views here.


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["POST"], url_path="login")
    def user_login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response({"error": "Please provide both username and password"}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=["POST"], url_path="register")
    def user_register(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        check_password = request.data.get("check_password")
        if not username or not password or not check_password:
            return Response({"error": "Please provide all fields"}, status=status.HTTP_400_BAD_REQUEST)
        if password != check_password:
            return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        login (request, user)
        return Response(status=status.HTTP_200_OK)
    

class TopicViewSet(viewsets.ModelViewSet):
    """API endpoint that allows topics to be viewed or edited."""

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
