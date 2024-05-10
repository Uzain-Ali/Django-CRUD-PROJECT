from django.db import models

# Create your models here.
class StudentDB(models.Model):
    name = models.CharField(max_length=25, blank=False, null = False)
    email = models.EmailField()
    gender = models.CharField(max_length=25, blank=False, null = False)
    phone = models.IntegerField()
    address = models.CharField(max_length=100, blank=False, null = False)

    def __str__(self):
        return self.name
    
