from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from TierList.models.nation import Nation
from TierList.forms import NationForm


def list_nations(request):
    nations = Nation.objects.all()
    context = {
        'nations': nations,
    }
    return render(request, 'nation/nations.html', context=context)
