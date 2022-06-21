from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from django.contrib.auth.models import amra_user                 

# Create your views here.

def home(request):
    return render(request,'login.html')


def login(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        signin=amra_user.object.filter(username=u,password=p)
        if signin:
            return render(request,'Home.html')