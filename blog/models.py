from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.CharField(max_length=255)
    min = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.title