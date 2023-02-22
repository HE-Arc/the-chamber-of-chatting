from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    id = models.Index()
    topic_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
class Message(models.Model):
    id = models.Index()
    user_id = models.ForeignKey(User, related_name="messages", on_delete=models.SET_NULL) # if user is banned, messages stay
    topic_id = models.ForeignKey(Topic, related_name="topic", on_delete=models.CASCADE) # if topic is deleted, messages are deleted too
    message = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)