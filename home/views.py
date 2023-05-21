from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from .models import Course 
from .models import  NewUser


# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        re_password=request.POST['re_password']
        email=request.POST['email']
        if password==re_password :
            
            user=NewUser.objects.create_user(username=username,email=email,password=password)
            
            
            messages.success(request, 'You have been rigisterd succsesfully .') # ignored
        
            return redirect('login')
        
    return render(request,'register.html')


def index(request):
    return render( request, "index.html")

def mainindex(request):
    return render( request, "mainindex.html")


def handellogin(request):
    if request.method == 'POST':
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']
        
        user =authenticate(username=login_username, password=login_password  )
        if user is not None and user.is_superuser==True:
            
            login(request, user)
            messages.success(request, 'You have been logged in successfully. admin')
            return redirect('dash')
        elif user is not None and user.is_staff==True and user.is_superuser==False:
            
            login(request, user)
            messages.success(request, 'You have been logged in successfully. teacher')
            return redirect('mainindex')
        elif user is not None and user.is_active==True and user.is_superuser==False  and user.is_staff==False:
            
            login(request, user)
            
            messages.success(request, 'You have been logged in successfully. student')
            return redirect('mainindex')
        
        else:
            messages.error(request, 'Invalid username or password.') 
    
    return render(request, 'login.html')

def handellogout(request):
    logout(request)
    messages.success(request,"You have been loggout in successfully.")
    # return redirect('login')
    return redirect('index')


def profile(request):
    return render(request,'profile.html')


def trainer(request):
    return render( request, "trainers.html")

def courses(request):
    return render( request, "courses.html")


def dash(request):
    data = len(Course.objects.all())
    data2 = len(NewUser.objects.all().values().filter(user_type="student"))
    data3 = len(NewUser.objects.all().values().filter(user_type="teacher"))
    
    context={'data':data,"data2":data2,"data3":data3}
    return render(request, 'dash.html', context)
    


def addcourse(request):
    if request.method=='POST':
        title=request.POST['title']
        description=request.POST['description']
        instructor=request.POST['instructor']
        fee=request.POST['fee']
        
        # updated_at=request.POST['email']
        
        cour=Course(title=title,description=description,instructor=instructor,fee=fee)
        cour.save()
        return redirect('dash')
    
    # context={ }
    return render( request, "addcourse.html")

 
def addteacher(request):
    if request.method=='POST':
        username=request.POST['username']
        experience=request.POST['experience']
        password=request.POST['password']
        re_password=request.POST['re_password']
        email=request.POST['email']
        if password==re_password :
            
            user=NewUser.objects.create_user(username=username,experience=experience,email=email,password=password,user_type='teacher')
            
            
            messages.success(request, 'Added teacher succsesfully .') # ignored
        
            return redirect('dash')
        
    return render(request,'addteacher.html')
   


def allcourse(request):
    data =  Course.objects.all().values()
    return render(request, 'allcourses.html', {'data': data})
    

def studentcourse(request):
    data = Course.objects.all().values()
    return render(request, 'studentcourse.html',{'data': data})
    
def student(request):
    data=NewUser.objects.all().values().filter(user_type="student")
    
    return render(request,'students.html',{"data":data})
    
def teacher(request):
    data=NewUser.objects.all().values().filter(user_type="teacher")
    
    return render(request,'teacher.html',{"data":data})
    
    

    