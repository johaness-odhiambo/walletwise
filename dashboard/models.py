from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField(default= now)
    description = models.TextField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length= 200)


    def __str__(self):
        return self.category
       
       # Custom function
    class Meta:
         ordering:['-date']    # type: ignore
    
class Category(models.Model):
    name = models.CharField(max_length= 200)

    class Meta:
         verbose_name_plural= 'Categories'   
    def __str__(self):
            return self.name
    
            
        