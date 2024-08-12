from django.shortcuts import render
import random
from .jokes import JOKES

# Create your views here.
def index(request):
    joke = random.choice(JOKES)
    return render(request, 'index.html', {'joke' : joke})