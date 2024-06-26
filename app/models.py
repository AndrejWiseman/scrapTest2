from django.db import models

# Create your models here.
class Horoskop(models.Model):

    znak = models.CharField(max_length=100)
    dnevni = models.TextField()

    def __str__(self):
        return self.znak