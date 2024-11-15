from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField(min_length=100)

    def __str__(self):
        return self.name

# Create your models here.
