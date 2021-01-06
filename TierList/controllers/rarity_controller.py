from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from TierList.models.rarity import Rarity
from TierList.forms import RarityForm


def list_raritys(request):
    raritys = Rarity.objects.all()
    context = {
        'raritys': raritys,
    }
    return render(request, 'rarity/raritys.html', context=context)

@login_required
def add_rarity(request):
    if request.method == 'POST':
        form = RarityForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect(reverse('raritys'))
    else:
        form = RarityForm()

    context = {
        'form': form
    }
    return render(request, 'rarity/rarity_form.html', context=context)

@login_required
def edit_rarity(request, rarity_id):
    if request.method == 'POST':
        rarity = Rarity.objects.get(pk=rarity_id)
        form = RarityForm(request.POST, instance=rarity)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('raritys'))
    else:
        rarity = Rarity.objects.get(pk=rarity_id)
        fields = model_to_dict(rarity)
        form = RarityForm(initial=fields, instance=rarity)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'rarity/rarity_form.html', context=context)    

@login_required
def delete_rarity(request, rarity_id):
    rarity = Rarity.objects.get(pk=rarity_id)
    if request.method == 'POST':
        rarity.delete()
        return HttpResponseRedirect(reverse('raritys'))
    context = {
        'rarity': rarity,
    }
    return render(request, 'rarity/rarity_delete_form.html', context=context)    
