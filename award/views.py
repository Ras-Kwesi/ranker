from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):

    return render('index.html')