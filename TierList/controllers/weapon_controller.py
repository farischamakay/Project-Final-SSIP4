from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from TierList.models.weapon import Weapon
from TierList.forms import WeaponForm


def list_weapons(request):
    weapons = Weapon.objects.all()
    context = {
        'weapons': weapons,
    }
    return render(request, 'weapon/weapons.html', context=context)
