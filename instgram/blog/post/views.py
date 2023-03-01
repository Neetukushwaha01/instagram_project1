from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate




# Create your views here.

def index(request):
    context = {}
    post = Post.objects.filter()
    context['post'] = post

    return render(request, 'index.html', context)


def login_page(request):
    if request.method=="POST":
        fname = request.POST.get('fname')
        password = request.POST.get('pswd')
        print(fname,password)
        user = authenticate(username=fname,password=password)

        print(user)


        if user:
            login(request, user)
            return redirect('/')
        else:
            print('not match')



    return render(request, 'login.html')

def sign_up(request):
    if request.method=='POST':
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')

        password= request.POST.get('pswd')
        username=fname
        print(username)

        print(fname,lname,password)
        u=User.objects.create_user(first_name=fname,last_name=lname,password=password,username=username,)
        return redirect('/login/')

    return render(request, 'signup.html')

def home_page(request):
    return render(request,'startpage.html')


def demo_page(request):
    return render(request,'demo_project.html')