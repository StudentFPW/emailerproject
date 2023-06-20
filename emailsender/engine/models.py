from django.db import models
from ckeditor.fields import RichTextField


class Sender(models.Model):
    content = RichTextField()
    emails = models.FileField(upload_to='emails_base/')
