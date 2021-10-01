from django.urls import path
from .views import ViolenceDetector

urlpatterns=[
    path("video", ViolenceDetector.as_view())
]