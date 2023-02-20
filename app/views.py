from urllib import request
from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import LoginForm,SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from .models import Employe

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeSerializer,Employe_post_Serializer


from rest_framework.views import APIView



class EmployeAPI(APIView):
    def get(self,request, pk = None):
        id= pk
        if id is not None:
            emp = Employe.objects.get(id=id)
            serializer = EmployeSerializer(emp)
            return Response(serializer.data)
        emp = Employe.objects.all()
        serializer = EmployeSerializer(emp,many=True)
        return Response(serializer.data)
    


    def post(self,request,*args, **kwargs):
        serializer = Employe_post_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context={"data":serializer.data,"message":"successs"}
            return Response(context)
        return Response('Not Success')

        # emp = Employe()
        # emp.name= serializer.name
        # emp.adress= serializer.adress
        # emp.phone = serializer.phone
        # emp.save()


def home(request):
    return render(request,'app/home.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = LoginForm(request=request ,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upassword=form.cleaned_data['password']
                user=authenticate(username=uname,password=upassword)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Loged in success")
                    return HttpResponseRedirect('/login/')
        else:
            form=LoginForm()
        return render(request,'app/login.html',{'form':form}) 
        return HttpResponseRedirect('/login/')


def user_signup(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congraluations ! You have become an Author, Thanks for be member!")
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request ,'app/signup.html',{'form':form})




def crud(request):
    info=Employe.objects.all()
    context = {"data":info}
    return render(request,'app/crud.html', context)


def Edit(request,id):
    info=Employe.objects.get(id=id)
    context = {"data":info}
    if request.method=="POST":
        name=request.POST.get('name')
        adress = request.POST.get('adress')
        phone = request.POST.get('phone')
        info.name=name
        info.adress=adress
        info.phone=phone
        info.save()
        return redirect('/crud/')
    return render(request,'app/edit.html',context)


        
def Delete(request,id):
    info=Employe.objects.get(id=id)
    info.delete()
    return redirect('/crud/')


def add_data(request):
    if request.method=="POST":
        name=request.POST.get('name')
        adress = request.POST.get('adress')
        phone = request.POST.get('phone')
        inst=Employe()
        inst.name=name
        inst.adress=adress
        inst.phone=phone
        inst.save()
        return redirect('/crud/')
    return render(request,'app/add.html')



def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')

def design(request):
    return render(request,'app/design.html')

def index(request):
    return render(request,'app/index.html')

def shop(request):
    return render(request,'app/shop.html')