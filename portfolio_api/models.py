

# Create your models here.


# Register your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title