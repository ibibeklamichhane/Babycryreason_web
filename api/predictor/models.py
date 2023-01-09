from django.db import models
from . models import *
import joblib
# Create your models here.



class Document(models.Model):
    file = models.FileField(upload_to='file/')

#class Data(models.Model):
#    
#    
#    filename = models.FileField()
#    prediction = models.CharField(max_length=100,blank=True)
#    def save(self, *args, **kwargs):
#        models = joblib.load('models/models.sav')
#        self.prediction = models.predict(
#            [[self.filename]]
#        )
#        return super().save(*args, **kwargs)
#
#

  

  