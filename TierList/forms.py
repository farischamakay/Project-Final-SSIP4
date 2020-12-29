from django.forms import ModelForm
from django.core.exceptions import ValidationError
from TierList.models import Character, Rarity


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

