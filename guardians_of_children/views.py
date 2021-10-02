import base64
import os
import sys

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from guardians_of_children.serializers import DataSerializer
from django.http import HttpResponse
from .process import run

sys.path.append(os.getcwd())

def convert2base64(img_dir):
    with open(img_dir, "rb") as image_file:
        base64str = base64.b64encode(image_file.read())
        return base64str

class ViolenceDetector(APIView):

    def __init__(self):
        self.base_dir = os.getcwd()

    def post(self, request):
        # print(request.data)

        out_dir = self.base_dir + "/media/frame.jpg"
        number, res = run(out_dir)

        if(number>0.75 and res==1):
            img = convert2base64(out_dir)
            return HttpResponse(content=img)
