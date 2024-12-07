from django.db import models

# Create your models here.
class Authentications(models.Model):
   
    # This is the logins table
    name =models.CharField(max_length= 200) 
    username =models.CharField( max_length=200)
    email =models.EmailField()
    password =models.CharField(max_length= 200)
      
     # To set appropriate plural
     # To return the values into human readable language

    class Meta:
        verbose_name_plural= 'Authentications'

    def __str__(self):
        return self.name

