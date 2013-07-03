from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.name

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    dish = models.CharField(max_length=255)
    price = models.DecimalField(default=0.00,decimal_places=2,max_digits=6)
    description = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.dish