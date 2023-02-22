from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("users", views.UserViewSet, "user")
router.register("topics", views.TopicViewSet, "topic")
router.register("messages", views.MessageViewSet, "message")


urlpatterns = [
    path("", include(router.urls)),
]