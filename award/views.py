from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    projects = Project.objects.all()

    return render(request,'index.html',{'projects':projects})


