from django.db import models

# Create your models here.
class Violence(models.Model):
    percentage = models.FloatField(default=0.0)
    uploaded_at = models.DateTimeField(auto_now_add=True)