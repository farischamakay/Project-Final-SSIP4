from django.db import models
from TierList.models.rarity import Rarity
from TierList.models.element import Element
from TierList.models.gender import Gender
from TierList.models.nation import Nation
from TierList.models.weapon import Weapon

class Character(models.Model):
    name = models.CharField(max_length=50)
    rarity = models.ForeignKey(Rarity, on_delete=models.SET_NULL, null=True)
    element = models.ManyToManyField(Element)
    gender = models.ManyToManyField(Gender)
    nation = models.ManyToManyField(Nation)
    weapon = models.ManyToManyField(Weapon)

   
    
class Meta:
    app_label = 'TierList'

def __str__(self):
    return f'{self.name}'
