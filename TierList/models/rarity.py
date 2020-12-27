from django.db import models

class Rarity(models.Model):
    level = models.CharField(max_length=200)
   
    class Meta:
        app_label = 'TierList'

    def __str__(self):
        return self.level