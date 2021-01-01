from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from TierList.models.element import Element
from TierList.forms import ElementForm


def list_elements(request):
    elements = Element.objects.all()
    context = {
        'elements': elements,
    }
    return render(request, 'element/elements.html', context=context)
