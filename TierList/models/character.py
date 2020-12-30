from django.db import models
from TierList.models.rarity import Rarity
from TierList.models.element import Element
from TierList.models.gender import Gender
from TierList.models.nation import Nation
from TierList.models.weapon import Weapon

class Character(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.ForeignKey(Rarity, on_delete=models.SET_NULL, null=True) 
    element = models.OneToOneField(Element, on_delete=models.CASCADE)
    gender = models.OneToOneField(Gender, on_delete=models.CASCADE)
    nation = models.OneToOneField(Nation, on_delete=models.CASCADE)
    weapon = models.OneToOneField(Weapon, on_delete=models.CASCADE)
    app_label = 'TierList'

    def str(self):
        return self.name