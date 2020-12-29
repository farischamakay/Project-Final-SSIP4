from django.forms import ModelForm
from django.core.exceptions import ValidationError
from TierList.models import Character, Rarity, Element, Gender, Nation, Weapon


class CharacterForm(ModelForm):
    class Meta:
        model = Character  # model to use in form
        # list of fields to be displayed
        fields = ['name', 'rarity']


class RarityForm(ModelForm):
    class Meta:
        model = Rarity  # model to use in form
        # list of fields to be displayed
        fields = ['level']


class ElementForm(ModelForm):
    class Meta:
        model = Element  # model to use in form
        # list of fields to be displayed
        fields = ['name']


class GenderForm(ModelForm):
    class Meta:
        model = Gender  # model to use in form
        # list of fields to be displayed
        fields = ['gender']


class NationForm(ModelForm):
    class Meta:
        model = Nation  # model to use in form
        # list of fields to be displayed
        fields = ['city']


class WeaponForm(ModelForm):
    class Meta:
        model = Weapon  # model to use in form
        # list of fields to be displayed
        fields = ['weapon']
