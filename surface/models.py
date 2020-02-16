from django.db import models


class Pane(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=250)

    def __str__(self):
        return self.title
