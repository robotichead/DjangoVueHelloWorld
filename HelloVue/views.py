from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core import serializers

from .models import *
# Create your views here.

def index(request):
    # Get Data
    places_results = Places.objects.all()

    # Get Templates
    t = loader.get_template('HelloVue/index.html')

    # Context
    c = {
        'places_results': serializers.serialize('json',places_results)
    }

    return HttpResponse(t.render(c, request))