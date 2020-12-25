from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from TierList.models import Character, Rarity
from TierList.forms import CharacterForm, RarityForm 


@login_required
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    num_characters = Character.objects.all().count()
    num_raritys = Rarity.objects.all().count()
    context = {
        'num_characters' : num_characters,
        'num_raritys': num_raritys,
        'total_visit': num_visits,
    }
    return render(request, 'index.html', context=context)

@login_required
def list_characters(request):
    characters = Character.objects.all()
    context = {
        'characters': characters,
    }
    return render(request, 'characters.html', context=context)


def add_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect(reverse('characters'))
    else:
        form = CharacterForm()

    context = {
        'form': form
    }
    return render(request, 'character_form.html', context=context)


def edit_character(request, character_id):
    if request.method == 'POST':
        character = Character.objects.get(pk=character_id)
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('characters'))
    else:
        character = Character.objects.get(pk=character_id)
        fields = model_to_dict(character)
        form = CharacterForm(initial=fields, instance=character)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'character_form.html', context=context)


def delete_character(request, character_id):
    character = Character.objects.get(pk=character_id)
    if request.method == 'POST':
        character.delete()
        return HttpResponseRedirect(reverse('characters'))
    context = {
        'character': character
    }
    return render(request, 'character_delete_form.html', context=context)    

@login_required
def list_raritys(request):
    raritys = Rarity.objects.all()
    context = {
        'raritys': raritys,
    }
    return render(request, 'raritys.html', context=context)


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
    return render(request, 'rarity_form.html', context=context)

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
    return render(request, 'rarity_form.html', context=context)    

def delete_rarity(request, rarity_id):
    rarity = Rarity.objects.get(pk=rarity_id)
    if request.method == 'POST':
        rarity.delete()
        return HttpResponseRedirect(reverse('raritys'))
    context = {
        'raritys': rarity,
    }
    return render(request, 'rarity_delete_form.html', context=context)        