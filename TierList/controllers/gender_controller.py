from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from TierList.models.gender import Gender
from TierList.forms import GenderForm


def list_genders(request):
    genders = Gender.objects.all()
    context = {
        'genders': genders,
    }
    return render(request, 'gender/genders.html', context=context)
