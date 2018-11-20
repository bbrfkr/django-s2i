from django.db import models

# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Bookmark(models.Model):
    abstract = models.CharField(max_length=30)
    url = models.CharField(max_length=999)
    description = models.CharField(max_length=999)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return self.abstract