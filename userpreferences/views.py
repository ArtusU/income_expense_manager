import json
import os

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render

from .models import UserPreference


def index(request):
    curency_data = []
    return render(request, 'preferences/index.html')