from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import Fffform
from .models import fff,Member,msg
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# p=[
#     {
#         'name' :"gopika" ,
#         'age' : 21
#     },
#     {
#         'name' : "joel" ,
#         'age': 21
#     }
# ]
def polls(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    f=fff.objects.all().filter(Q(member__fname__icontains=q) |
                               Q(det__icontains=q) |
                               Q(member__lname__icontains=q)
                               
                               )
    member=Member.objects.all()
    
    msgs=msg.objects.all().filter(Q(hhh__member__fname__icontains=q) |
                                  Q(hhh__det__icontains=q) |
                               Q(hhh__member__lname__icontains=q)
                                  )
    count=f.count()
    context={
        "f":f,
        "member" :member,
        "count" :count,
        "msgs":msgs,
       
    }
    
    template=loader.get_template('myhtml.html')
    return HttpResponse(template.render(context,request))

def about(request,pk):
    hhh=fff.objects.get(id=pk)
    msgs=hhh.msg_set.all().order_by('-time')
    p=hhh.participants.all()
    
    if(request.method=='POST'):
        l=msg.objects.create(
            host=request.user,
            hhh=hhh,
            body=request.POST.get('comment')
        )
        hhh.participants.add(request.user)
        #if f.is_valid():
       
        return redirect('ffn',pk=hhh.id)
    context={
        "hhh":hhh,
        "msgs":msgs,
        "p":p
    }
    return render(request,'ffn.html',context)


@login_required(login_url='myuser')
def forms(request):
    f=Fffform()
    if(request.method=='POST'):
        f=Fffform(request.POST)
        if f.is_valid():
            f.save()
            return redirect('myname')
    context={
        "f":f
    }
    return render(request,'forms.html',context)
@login_required(login_url='myuser')
def edit(request,pk):
    l=fff.objects.get(id=pk)
    f=Fffform(instance=l)
    if(request.user != l.host):
        return HttpResponse("You are not allowed here")
    if(request.method =='POST'):
        f=Fffform(request.POST,instance=l)
        if f.is_valid():
            f.save()
            return redirect('myname')
    
    context={
        "f":f
    }
    return render(request,'forms.html',context)
@login_required(login_url='myuser')
def delete(request,pk):
    f=fff.objects.get(id=pk)
    if(request.method =='POST'):
        f.delete()
        return redirect('myname')
    return render(request,'delete.html',{"f":f})

def loginpage(request):
    if(request.user.is_authenticated):
        return redirect('myname')
    page='login'
    context={
        "page":page
    }
    if(request.method =='POST'):
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'User not valid')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('myname')
        else:
            messages.error(request,'Username or password is incorrect')
    return render(request,'login.html',context)

def logoutpage(request):
    logout(request)
    return redirect('myname') 

def registerpage(request):
    page='register'
    form=UserCreationForm()
    
    if(request.method =='POST'):
        form=UserCreationForm(request.POST)
        if (form.is_valid()):
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('myname') 
        else:
            messages.error(request,"Registration unsuccessfull")
    context={
        "page":page,
        "form":form
    }
    return render(request,'login.html',context)

login_required(login_url='myuser')
def deletemsg(request,pk):
    f=msg.objects.get(id=pk)
    # hhh=fff.objects.get(id=pk)
    # p=hhh.participants.all()
    if request.user != f.host:
        return HttpResponse("You are not allowed")
    if(request.method =='POST'):
        f.delete()
        
        return redirect('myname')
    return render(request,'delete.html',{"f":f})


def profile(request,pk):
    # f=fff.objects.all().get(host=pk)
    
    msgs=msg.objects.all().filter(host_id=pk)
    f=msgs.first()
    member=Member.objects.all()
    return render(request,'profile.html',{"msgs":msgs,"member":member,"f":f})