from django.db import models

class File(models.Model):
  # file = models.ImageField(upload_to='media/')
  file = models.ImageField()
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)
  