from django.db import models

# Create your models here.

class Machine(models.Model):
    name = models.CharField(max_length=100) # makine adı
    description = models.TextField() # makine açıklaması
    image = models.ImageField(upload_to='machines', null=True,blank=True)   # makine fotoğrafı
    technical_specs = models.TextField() # teknik özellikler

# main/models.py


    def __str__(self) :
        return self.name