from django.db import models

class Covid(models.Model):
    nombre = models.CharField(max_length=60)
    año = models.DateField()
    rut = models.TextField
    infect = models.BooleanField()
    family = models.BooleanField()
   
    def publish(self):
        self.save()
