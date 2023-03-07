from django.contrib import admin

from .models import Message, Topic

# Register your models here.

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0

class TopicAdmin(admin.ModelAdmin):
    list_display = ("topic_name", "created")
    list_filter = ("created",)
    search_fields = ("topic_name",)
    
    inlines = [MessageInline]

admin.site.register(Topic, TopicAdmin)

