from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from accounts.forms import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from blogpost.models import Post,Category
# Create your views here.

def index(request):
    context = {}
    if Post.objects.exists():
        latest = Post.objects.latest('date')
        context['latest'] = latest
        context['posts'] = Post.objects.all()  
        context['categories'] = Category.objects.all()  
    return render(request,'home.html',context)


def signup(request):
    context = {}
    if request.method == 'POST':
        user_form = MyUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return index(request)
    else:
        user_form = MyUserCreationForm()
        profile_form = ProfileForm()
    context['user_form'] = user_form
    context['profile_form'] = profile_form
    return render(request,'registration.html',context)

def login_view(request):
    context = {}
    if request.method == 'POST':
        form = MyAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return index(request)
    else:
        form = MyAuthenticationForm()
    context['form'] = form
    return render(request,'login.html',context)

def logout_view(request):
    logout(request)
    return login_view(request)

def profile_view(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        context = {'message' : 'You havent logged in!' }
        return render(request,'not_allowed.html',context)

def author_view(request):
    return render(request,'author.html')