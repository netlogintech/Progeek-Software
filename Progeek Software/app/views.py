from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from . import models
from . import forms
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.
def home(request):
    head=models.Header.objects.all()
    return render(request,"app/index.html",{"head":head})
def career(request):
    head=models.Header.objects.all()
    joinForm=forms.JoinForm()
    if request.method=='POST':
        joinForm=forms.JoinForm(request.POST, request.FILES)
        if joinForm.is_valid():
            joinForm.save()
        return HttpResponseRedirect('/career')
    return render(request,"app/career.html",{"head":head,'joinForm':joinForm})

def user(request):
    head=models.Header.objects.all()
    return render(request,"app/user.html",{"head":head})

def register(request):
    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            models.Customer.objects.create(user=user)
            messages.success(request, 'Registration Successful')
            return redirect('/login')
    else:
        form = forms.CreateUserForm()

    return render(request,'app/signup.html',{'form': form})
def is_trainer(user):
    return user.groups.filter(name='TRAINER').exists()
def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

def afterlogin_view(request):
    if is_trainer(request.user):
        return redirect('/trainer')
    else:
        return redirect('/live')

#--------------TRAINER DASHBOARD-----------------------------#
@login_required(login_url='/login')
@user_passes_test(is_trainer)
def trainer(request):
    train=models.Train.objects.all()
    head=models.Header.objects.all()
    users=request.user.username
    return render(request,"app/trainer.html",{"train":train,"user":users,"head":head})
@login_required(login_url='/login')
@user_passes_test(is_trainer)
def join(request):
    join=models.Join.objects.all()
    head=models.Header.objects.all()
    users=request.user.username
    return render(request,"app/trainer_join.html",{"join":join,"user":users,"head":head})
@login_required(login_url='login')
@user_passes_test(is_trainer)
def delete_data(request,pk):
    gp=models.Train.objects.get(id=pk)
    gp.delete()
    return redirect('/trainer')

@login_required(login_url='login')
@user_passes_test(is_trainer)
def add_meeting(request):
    head=models.Header.objects.all()
    meetingForm=forms.TrainForm()
    if request.method=='POST':
        meetingForm=forms.TrainForm(request.POST, request.FILES)
        if meetingForm.is_valid():
            meetingForm.save()
        return HttpResponseRedirect('/trainer')
    users=request.user.username
    return render(request,'app/add_meeting.html',{'meetingForm':meetingForm,"user":users,"head":head})

def it_outsourcing(request):
    head=models.Header.objects.all()
    return render(request,"app/it_outsourcing.html",{"head":head})
def ims(request):
    head=models.Header.objects.all()
    return render(request,"app/ims.html",{"head":head})
def testing(request):
    head=models.Header.objects.all()
    return render(request,"app/testing.html",{"head":head})

def managed(request):
    head=models.Header.objects.all()
    return render(request,"app/managed.html",{"head":head})

def enterprise(request):
    head=models.Header.objects.all()
    return render(request,"app/enterprise.html",{"head":head})
def captive(request):
    head=models.Header.objects.all()
    return render(request,"app/captive.html",{"head":head})
def strategic(request):
    head=models.Header.objects.all()
    return render(request,"app/strategic.html",{"head":head})
def outsourced(request):
    head=models.Header.objects.all()
    return render(request,"app/outsourced.html",{"head":head})
def system(request):
    head=models.Header.objects.all()
    return render(request,"app/system.html",{"head":head})
def enterprise_solution(request):
    head=models.Header.objects.all()
    return render(request,"app/enterprise_solution.html",{"head":head})
def big_data(request):
    head=models.Header.objects.all()
    return render(request,"app/big_data.html",{"head":head})
def data_science(request):
    head=models.Header.objects.all()
    return render(request,"app/data_science.html",{"head":head})
def social(request):
    head=models.Header.objects.all()
    return render(request,"app/social.html",{"head":head})

def automations(request):
    head=models.Header.objects.all()
    return render(request,"app/automations.html",{"head":head})
def cloud(request):
    head=models.Header.objects.all()
    return render(request,"app/cloud.html",{"head":head})
def mobolity(request):
    head=models.Header.objects.all()
    return render(request,"app/mobility.html",{"head":head})
def robotics(request):
    head=models.Header.objects.all()
    return render(request,"app/robotics.html",{"head":head})
def ibm(request):
    head=models.Header.objects.all()
    return render(request,"app/ibm.html",{"head":head})
def ms_app(request):
    head=models.Header.objects.all()
    return render(request,"app/ms_app.html",{"head":head})
def ms_tech(request):
    head=models.Header.objects.all()
    return render(request,"app/ms_tech.html",{"head":head})
def about(request):
    head=models.Header.objects.all()
    return render(request,"app/about.html",{"head":head})
@login_required(login_url='/login')
def live(request):
    head=models.Header.objects.all()
    train=models.Train.objects.order_by('-id')
    return render(request,"app/live.html",{"head":head,"train":train})
def meeting(request):
    head=models.Header.objects.all()

    return render(request,"app/meeting.html",{"head":head})
def search(request):
    head=models.Header.objects.all()

    return render(request,"app/search.html",{"head":head})
