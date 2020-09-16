from django.db import models

# Create your models here.

class Places(models.Model):
    PlaceName = models.CharField(
        max_length=50,
    )
