from django.db import models
from ckeditor.fields import RichTextField


class Sender(models.Model):
    title = models.CharField(max_length=64)
    content = RichTextField()
    emails = models.FileField(upload_to='emails_base/%Y/%m/%d/')
    datetime = models.DateField(auto_now_add=True)
