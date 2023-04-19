from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Topic
from .models import Message


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "url",
            "username",
            "email",
            "first_name",
            "last_name",
            "topics",
            "messages",
        ]


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = [
            "id",
            "url",
            "topic_name",
            "user_id",
            "created",
            "messages",
        ]


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = [
            "id",
            "url",
            "user_id",
            "topic_id",
            "message",
            "created",
        ]
