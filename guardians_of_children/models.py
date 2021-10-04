from django.db import models

# Create your models here.
class Violence(models.Model):
    percentage = models.FloatField(default=0.0)
    res = models.CharField(blank=True, max_length=10)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")

    def __str__(self):
        return self.caption
