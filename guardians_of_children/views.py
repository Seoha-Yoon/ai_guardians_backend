import base64
import os
import sys

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse

from .models import Video
from .process import run

sys.path.append(os.getcwd())


class ViolenceDetector(APIView):

    def __init__(self):
        self.base_dir = os.getcwd()

    def post(self, request):
        # print(request.data)
        number, res = run()

        if(number>0.5 and res==1):
            str = "fight detect"
            return HttpResponse(content=str)

def index(request):
    video = Video.objects.all()
    return render(request,"index.html",{"video":video})
