from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.ForeignKey('rarity', on_delete=models.SET_NULL, null=True) 

    class Meta:
        app_label = 'TierList'

    def __str__(self):
        return f'{self.name}'    

