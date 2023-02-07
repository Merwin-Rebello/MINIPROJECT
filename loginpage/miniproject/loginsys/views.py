from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
# def index(request):
#     list=feats.objects.all()
#     key=1
#     return render(request,"login.html",{'feature':list,'key':key})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'login.html',{'text':'sucessfully logged in'})
        else:
            return render(request,'login.html',{'text':' SORRRY!! cannot login'})
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        # list=feats.objects.all()
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if (password==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('index')        
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('index')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)  
                key=0 
                user.save()
            # return render(request,'login.html',{'feature':list,"key":key,'key2':1})
        else:
            messages.info(request,'Password Not Same')
            return redirect('index')
    return render(request,'login.html')