from django.urls import path
from . import views
from .views import ViolenceDetector

urlpatterns=[
    path("", views.index),
    path("violence",ViolenceDetector.as_view()),
]