from rest_framework import permissions
from PIL import Image
import sys
from django.views.decorators.csrf import csrf_exempt
import pyocr
import pyocr.builders
import base64

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
   # print(queryset)
   serializer_class = FileSerializer
   permission_classes = (permissions.AllowAny, )

class FileCreateView(APIView):

   @csrf_exempt
   def post(self,request):
      
      attached_file = request.data['attached_file']
      # attached_file = Image.fromstring('RGB',(width,height),decodestring(attached_file))
      # attached_file.save("foo.png")
      print(attached_file)
      # attached_file = base64.b64decode(attached_file)
      # queryset = File.objects.all()
      tools = pyocr.get_available_tools()
      print(tools)
      if len(tools) == 0:
          print("No OCR tool found")
      tool = tools[0]    
      langs = tools.get_available_languages()
      lang = langs[0]
      txt = tool.image_to_string(Image.open(attached_file),builder=pyocr.builders.TextBuilder())
      return Response({"result":txt}, status=200)
   