from django.forms import ModelForm
from django.core.exceptions import ValidationError
from TierList.models import Character, Rarity, Element, Gender, Nation, Weapon


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'rarity', 'element', 'gender', 'nation', 'weapon']


class RarityForm(ModelForm):
    class Meta:
        model = Rarity
        fields = ['level']


class ElementForm(ModelForm):
    class Meta:
        model = Element
        fields = ['name']


class GenderForm(ModelForm):
    class Meta:
        model = Gender
        fields = ['name']


class NationForm(ModelForm):
    class Meta:
        model = Nation
        fields = ['name']


class WeaponForm(ModelForm):
    class Meta:
        model = Weapon
        fields = ['name']
