from rest_framework import permissions
from PIL import Image
import sys

import pyocr
import pyocr.builders
import pytesseract
# import cv2
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import (
   ListAPIView,
   CreateAPIView,
   
)
from restapp.models import File
from restapp.api.serializers import FileSerializer


class FileListView(ListAPIView):
   queryset = File.objects.all()
   # print(queryset)
   serializer_class = FileSerializer
   permission_classes = (permissions.AllowAny, )

class FileCreateView(APIView):

   def post(self,request):
      print(request.data)
      attached_file = request.FILES['attached_file']
      #queryset = File.objects.all()
      tools = pyocr.get_available_tools()
      tool = tools[0]
      langs = tool.get_available_languages()
      lang = langs[0]
      txt = tool.image_to_string(Image.open(attached_file),lang = lang,builder=pyocr.builders.TextBuilder())
      print(txt)
      return Response({"msg":txt}, status=200)
   #  print('xyz')
   #  queryset = File.objects.all()
   #  serializer_class = FileSerializer
   #  permission_classes = (permissions.AllowAny, )
   # #  print(queryset[30].file)
      image=cv2.imread(queryset[30].file,1)
      string=pytesseract.image_to_string(image)
      print(string)
   #  length = len(queryset)
      img = Image.open(attached_file)  
   # #  print(img)
   # # #  pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
      result = pytesseract.image_to_string(img)  
      print(result)
   #  tools = pyocr.get_available_tools()
   #  if len(tools) == 0:
   #    print("No OCR tool found")
   # # #  sys.exit(1)
   # # #  # The tools are returned in the recommended order of usage
   #  tool = tools[0]
   #  langs = tool.get_available_languages()
   #  lang = langs[0]
   #  txt = tool.image_to_string(Image.open(queryset[length-1].file),lang = lang,builder=pyocr.builders.TextBuilder())
   #  print(txt)
   #  return Response({"msg":txt}, status=status.HTTP_201_CREATED)
   #  C:\Program Files (x86)\Tesseract-OCR

   
    
