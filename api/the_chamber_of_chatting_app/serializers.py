from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Topic
from .models import Message

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
        ]
        
class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = [
            "topic_name"
            "created"
        ]
        
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = [
            "message"
            "created"
        ]