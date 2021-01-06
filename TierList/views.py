from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from TierList.models.character import Character
from TierList.models.rarity import Rarity
from TierList.models.element import Element
from TierList.models.gender import Gender
from TierList.models.nation import Nation
from TierList.models.weapon import Weapon
from TierList.forms import CharacterForm, RarityForm, ElementForm, GenderForm, NationForm, WeaponForm


@login_required
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    num_characters = Character.objects.all().count()
    num_raritys = Rarity.objects.all().count()
    num_elements = Element.objects.all().count()
    num_genders = Gender.objects.all().count()
    num_nations = Nation.objects.all().count()
    num_weapons = Weapon.objects.all().count()    

    context = {
        'num_characters' : num_characters,
        'num_raritys': num_raritys,
        'num_elements': num_elements,
        'num_genders': num_genders,
        'num_nations': num_nations,
        'num_weapons': num_weapons,
    }
    return render(request, 'home/index.html', context=context)

