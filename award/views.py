from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    projects = Project.objects.all()

    return render(request,'index.html',{'projects':projects})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    print(profile)
    # profile = Profile.objects.filter(user=request.user.id)
    projects = Project.objects.filter(profile = current_user)

    return render(request, 'profile.html', {'profile': profile, 'images': projects})


@login_required(login_url='/accounts/register/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProject(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('index')

    else:
        form = NewProject()
    return render(request, 'new_post.html', {"form": form})

def search(request):

    if 'project' in request.GET and request.GET["project"]:
        search_query = request.GET.get("project")
        searched_projects = Project.objects.filter(user__username=search_query)
        message = f"{search_query}"
        print(searched_projects)

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
