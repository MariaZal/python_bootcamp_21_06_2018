from django.db import models

# Create your models here.

PRIORITY = (("LOW", "LOW"), ('NORMAL', 'NORMAL'), ("HIGH", "HIGH"))

class Example(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(choices=PRIORITY, max_length=6)
    is_actual = models.BooleanField()

    def __str__(self):
        return self.name