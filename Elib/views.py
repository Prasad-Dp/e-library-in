from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import book
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def index(request):
    books=book.objects.all
    return render(request,'index.html',{'books':books})

def home(request):
    if(request.user.is_authenticated):
        books=book.objects.values('book_gener')
        a=[x['book_gener'] for x in books]
        res = []
        [res.append(x) for x in a if x not in res]
        xyz=[]
        for abc in res:
            xyz.append(book.objects.all().filter(book_gener=abc))
        dic={'label':[res]}
        print(dic)
        return render(request,'home.html',{'xyz':xyz,'abc':res})
    return redirect('login')
    
    
    

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            uname=request.POST['uname']
            passw=request.POST['passw']
            user=authenticate(username=uname,password=passw)
            if user is None:
                messages.info(request,"Creat Account")
                return redirect('login')
            else:
                login(request,user)
                return redirect('home')
        return render(request,'login.html')


def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        unmae=request.POST['username']
        passw=request.POST['password']
        if User.objects.filter(username=unmae).exists():
            messages.info(request,"User Name already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email already exists")
            return redirect('register')
        else:
            user = User.objects.create_user(username=unmae,password=passw,email=email,first_name=name)
            user.save()
            return redirect('home')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def book_view(request,slug):
    
    view_book=book.objects.all().filter(book_slug=slug)
    books=book.objects.all()
    return render(request,'book_view.html',{'view_book':view_book,'all_books':books})
