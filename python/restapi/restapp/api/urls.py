from django.urls import path
from .views import (
   FileListView,
   FileCreateView
)

urlpatterns = [
   path('', FileListView.as_view()),
   path('create',FileCreateView.as_view())

]