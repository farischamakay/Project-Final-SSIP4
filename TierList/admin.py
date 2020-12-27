from django.contrib import admin
from TierList.models.character import Character
from TierList.models.rarity import Rarity
from TierList.models.element import Element
from TierList.models.gender import Gender
from TierList.models.nation import Nation
from TierList.models.weapon import Weapon

admin.site.register(Character)
admin.site.register(Rarity)
admin.site.register(Element)
admin.site.register(Gender)
admin.site.register(Nation)
admin.site.register(Weapon)