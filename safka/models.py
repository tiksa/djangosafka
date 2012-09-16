from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

class Vote(models.Model):
    voter = models.CharField(max_length=20, unique=True)
    time = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant)
    
    def __unicode__(self):
        return self.voter + ": klo " + str(self.time) + " @" + str(self.restaurant)
