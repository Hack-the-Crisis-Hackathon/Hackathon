from django.db import models

# Create your models here.

class Document(models.Model):
    name = models.CharField(max_length=255, blank=False, default="Some Image")
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='test')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document.url
