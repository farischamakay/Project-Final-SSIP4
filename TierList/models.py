from django.db import models


class Rarity(models.Model):
    level = models.CharField(max_length=200)
   

    def __str__(self):
        return self.level

class Character(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.ForeignKey('rarity', on_delete=models.SET_NULL, null=True)
    
    

    def __str__(self):
        return f'{self.name}'    

