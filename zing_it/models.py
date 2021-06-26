from django.db import models

# Create your models here.


class Player(models.Model):
    bio = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    name = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    position = models.CharField(max_length=70)
    age = models.CharField(max_length=70)
    number = models.CharField(max_length=70)
    flag = models.CharField(max_length=170)
    country = models.CharField(max_length=70)

    def __str__(self):
        return "{} {}".format(self.name, self.lname)
