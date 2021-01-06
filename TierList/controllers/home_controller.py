from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from TierList.models.character import Character


def index(request):
    if request.method == 'POST':
        req = request.POST.dict()

        name = req['name']
        characters = Character.objects.filter(name__contains=name)
    else:
        characters = Character.objects.all()  
    # put in data dictionary
    data = {
        'characters': characters,
    }
    # render to our html
    return render(request, 'home/index.html', context=data)

