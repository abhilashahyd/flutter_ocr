from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import (
   FileListView,
   FileCreateView
)

urlpatterns = [
   path('', FileListView.as_view()),
   path('create',csrf_exempt(FileCreateView.as_view()))

]