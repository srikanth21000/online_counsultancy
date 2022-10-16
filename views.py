from email import message
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    form =CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'account created successfully')
            return redirect('login')
    context={'form':form}
    return render(request,'home1/register.html',context)
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Username or Password is incorrect")

    return render(request,'home1/login.html')
@login_required(login_url='login')
def home(request):
    return render(request,'home1/home.html')
@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def property(request):
    return render(request,'home1/properties.html')
@login_required(login_url='login')
def submit(request):
    return render(request,'home1/submit_properties.html')
@login_required(login_url='login')
def contact(request):
    return render(request,'home1/contact_us.html')
@login_required(login_url='login')
def profile(request):
    return render(request,'home1/profile.html')
@login_required(login_url='login')
def muzamil(request):
    return render (request, 'home1/muzamil.html')
@login_required(login_url='home')
def muzamillog(request):
    return render (request, 'home1/muzamillog.html')
