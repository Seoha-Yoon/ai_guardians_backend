from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from guardians_of_children.serializers import DataSerializer
from django.http import HttpResponse
from .process import run


class ViolenceDetector(APIView):
    def post(self, request):
        # print(request.data)
        number, res = run()

        return HttpResponse(content=res)