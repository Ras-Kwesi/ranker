from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db import transaction


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

@login_required(login_url='/accounts/login/')
@transaction.atomic
def update(request):
    # current_user = User.objects.get(pk=user_id)
    current_user=request.user
    if request.method == 'POST':
        user_form = EditUser(request.POST, request.FILES,instance=request.user)
        profile_form = EditProfile(request.POST, request.FILES,instance=current_user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
        return redirect('profile')

    else:
        user_form = EditUser(instance=request.user)
        profile_form = EditProfile(instance=current_user.profile)
    return render(request, 'update_profile.html', {
        "user_form": user_form,
        "profile_form": profile_form
    })

# @login_required(login_url='/accounts/login/')
# def project(request,id):
#     current_user = request.user
#     project = Project.objects.get(id=id)
#     if request.method == 'POST':
#         voting_form = NewVote(request.POST)
#         if voting_form.is_valid():
#             vote = voting_form.save(commit=False)
#             vote.voter = current_user
#             vote.project = project
#             vote.save()
#         return redirect('index')
#     else:
#         voting_form = NewVote()
#
#     return render(request,'single_project.html',{'project':project, 'voting_form':voting_form})

@login_required(login_url='/accounts/login/')
def project(request,id):
    current_user = request.user
    project = Project.objects.get(id=id)
    voting_form = NewVote()

    return render(request,'single_project.html',{'project':project, 'voting_form':voting_form})

def vote(request):
    designvote = request.POST.get('designvote')
    usabilityvote = request.POST.get("usabilityvote")
    creativityvote = request.POST.get('creativityvote')
    contentvote = request.POST.get('contentvote')

    vote = Vote(designvote = designvote,
                usabilityvote = usabilityvote,
                creativityvote = creativityvote,
                contentvote = contentvote,
                )
    vote.save()
    data = {'success':'Thank you for voting'}

    return JsonResponse(data)