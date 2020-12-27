from django.contrib import admin
from .models import Character, Rarity, Element, Gender, Nation, Weapon

admin.site.register(Character)
admin.site.register(Rarity)
admin.site.register(Element)
admin.site.register(Gender)
admin.site.register(Nation)
admin.site.register(Weapon)