from django.db import models

# Create your models here.


STATUS = (("dostepny", "dostepny"), ('niedostepny', 'niedostepny'))

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=20)
    status = models.CharField(choices=STATUS, max_length=20)
    is_actual = models.BooleanField()

    def __str__(self):
        return self.name