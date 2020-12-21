from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import sys
import pyocr
import pyocr.builders
import base64
import pytesseract

from rest_framework.views import APIView
from rest_framework.response import Response
from restapp.models import File
from restapp.api.serializers import FileSerializer

from rest_framework.generics import (
   ListAPIView,
   CreateAPIView,
   )
class FileListView(ListAPIView):
   queryset = File.objects.all()
   serializer_class = FileSerializer
   permission_classes = (permissions.AllowAny, )

class FileCreateView(APIView):

  
   @csrf_exempt
   def post(self,request):
      
      attached_file = request.data['attached_file']
      # img = Image.open(attached_file)
      # print(img)
      # txt = pytesseract.image_to_string(img,lang = 'eng')
      tools = pyocr.get_available_tools()
      print(tools)
      if len(tools) == 0:
          print("No OCR tool found")
      tool = tools[0]    
      langs = tool.get_available_languages()
      lang = langs[0]
      txt = tool.image_to_string(Image.open(attached_file),lang = lang,builder=pyocr.builders.TextBuilder())
      return Response({"result":txt}, status=200)
   