from django.db import models

# Create your models here.

class Enquiries(models.Model):
    name=models.TextField(max_length= 200)
    email=models.EmailField()
    subject=models.TextField(255)
    message=models.TextField(255)

    def __str__(self):
        return self.name
