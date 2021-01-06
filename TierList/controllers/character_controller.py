from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from TierList.models.character import Character
from TierList.forms import CharacterForm

def list_characters(request):
    characters = Character.objects.all()
    context = {
        'characters': characters,
    }
    return render(request, 'character/character_characters.html', context=context)


@login_required
def add_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect(reverse('character_characters'))
    else:
        form = CharacterForm()

    context = {
        'form': form
    }
    return render(request, 'character/character_form.html', context=context)

@login_required
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
    return render(request, 'character/character_form.html', context=context)

@login_required
def delete_character(request, character_id):
    character = Character.objects.get(pk=character_id)
    if request.method == 'POST':
        character.delete()
        return HttpResponseRedirect(reverse('characters'))
    context = {
        'character': character
    }
    return render(request, 'character/character_delete_form.html', context=context)    

