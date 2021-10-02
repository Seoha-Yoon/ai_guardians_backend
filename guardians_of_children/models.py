from django.db import models

# Create your models here.
class Violence(models.Model):
    percentage = models.FloatField(default=0.0)
    res = models.CharField(blank=True, max_length=10)
    uploaded_at = models.DateTimeField(auto_now_add=True)