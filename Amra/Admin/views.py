from email.message import Message
from http.client import CONFLICT
from django.shortcuts import render,redirect
from Admin.models import amra_user             
from django.contrib import messages
# Create your views here.

def login(request):
    return render(request,'login.html')


def home(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        user=amra_user.objects.filter(username=u).values('id')[0]
        us=int(user.get('id'))
        pid=amra_user.objects.filter(password=p).values('id')[0]
        p=int(pid.get('id'))
        if p==us:
            return render(request,'Home.html',{'u':u})
        else:
            messages.error(request,'Invalid username')
            return render(request,'login.html',{"Message":messages})
    return render(request,'login.html')

        # user=amra_user.objects.filter(username=u).values()
        # pas=amra_user.objects.filter(password=p).values()
        
    #     context={
    #         'username':user,
    #         'password':pas,
    #         'pid':pid,
    #     }
    # messages.success(request, 'Login Success')
    # return render(request,'login.html',context)