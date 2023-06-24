from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from .models import Course 
from .models import  NewUser
from .models import  Course_student
from .models import  File
import pandas  as pd
from datetime import datetime
from django.contrib.auth.hashers import make_password
from .models import Student_course_fee


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

def remove_user(request, student_id):
    user = NewUser.objects.get(id=student_id)
    user.delete()
    return redirect('rec_students')


def index(request):
    return render( request, "index.html")

def mainindex(request):
    return render( request, "mainindex.html")

def mainindex2(request):
    return render( request, "mainindex2.html")


def handellogin(request):
    if request.method == 'POST':
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']
        
        user =authenticate(username=login_username, password=login_password  )
        if user is not None and user.is_superuser==True:
            
            login(request, user)
            messages.success(request, 'You have been logged in successfully. admin')
            return redirect('dash')
        elif user is not None and user.is_staff==True and user.is_superuser==False and user.user_type=='teacher':
            
            login(request, user)
            messages.success(request, 'You have been logged in successfully. teacher')
            return redirect('mainindex')
        elif user is not None and user.is_active==True and user.is_superuser==False  and user.is_staff==False:
            
            login(request, user)
            
            messages.success(request, 'You have been logged in successfully. student')
            return redirect('mainindex2')
        
        elif user is not None and user.is_active==True and user.is_superuser==False  and user.is_staff==True and user.user_type=='receptionist':
            
            login(request, user)
            
            messages.success(request, 'You have been logged in successfully. receptionist')
            return redirect('rec_dash')
        
        else:
            messages.error(request, 'Invalid username or password.') 
    
    return render(request, 'login1.html')

def handellogout(request):
    logout(request)
    messages.success(request,"You have been loggout in successfully.")
    
    return redirect('index')



@login_required
def profile(request):
    user = request.user
    data_c_e = Student_course_fee.objects.filter(user=user).count()

    return render(request, 'profile.html', {"data_c_e": data_c_e})

@login_required
def pro_student(request):
    user = request.user
    data_c_e = Student_course_fee.objects.filter(user=user).count()

    return render(request, 'pro_student.html', {"data_c_e": data_c_e})
    
def courses(request):
    return render( request, "courses.html")
@login_required
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
        cour=Course(title=title,description=description,instructor=instructor,fee=fee)
        cour.save()
        return redirect('dash')
    
    # context={ }
    return render( request, "addcourse.html")

def update_course(request, course_id):
    # obj single tuple 
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        instructor = request.POST['instructor']
        fee = request.POST['fee']

        course.title = title
        course.description = description
        course.instructor = instructor
        course.fee = fee
        course.save()
        return redirect('allcourse')
    return render(request, 'update_course.html', {'course': course})

def course_taken(request,student_id):
    student_tuple = Course.objects.get(id=student_id)
    
    return render( request, "coursetaken.html")
 
def addteacher(request):
    if request.method=='POST':
        username=request.POST['username']
        experience=request.POST['experience']
        password=request.POST['password']
        re_password=request.POST['re_password']
        email=request.POST['email']
        if password==re_password :
            
            user = NewUser.objects.create_user(username=username, password=password, is_staff=True,experience=experience,email=email,user_type='teacher')

            
            messages.success(request, 'Added teacher succsesfully .') 
        
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
    
    return render(request,'teachers.html',{"data":data})
    
def create_db(file_path):
    df = pd.read_excel(file_path, engine='openpyxl')
    list_of_csv = [list(row) for row in df.values]
    for l in list_of_csv:
        now = datetime.now()
        password = '12345678'
        password = make_password(password)
        is_staff = 0
        is_active = 1
        
        user_type = 'student'
        NewUser.objects.create(username=l[0], first_name=l[1], last_name=l[2], email=l[3], password=password,is_staff=is_staff, is_active=is_active, user_type=user_type,date_joined=now)
    return redirect('student')
    
    
    
    
def import_data(request):
    if request.method == 'POST':
        file_to_send = request.FILES['file']
      
        obj=File.objects.create(file=file_to_send)
        # return HttpResponse("Done!")
        create_db(obj.file)
        # return redirect('/student')
        return redirect('student')
    return render(request, 'importdata.html')



@login_required
def enrollcourse(request):
    if request.method == 'POST':
        selected_course_id = int(request.POST.get('selected_course'))
        user = request.user  # Get the currently logged-in user
        amount=request.POST.get('amount_paid')
        
        if selected_course_id and user:
            course = Course.objects.get(id=selected_course_id)
            print('\n\n',course.fee,'\n\n')
            enrolled_courses = Student_course_fee.objects.filter(user=user, selected_course_id=course)
            if not enrolled_courses.exists():
                Student_course_fee.objects.create(user=user, selected_course_id=course,paid_amount=amount,course_fee=course.fee)
                messages.success(request, 'Course enrolled successfully.')
            else:
                messages.error(request, 'You are already enrolled in this course.')

            return redirect('pro_student')

    data = Course.objects.all()
    enrolled_course_ids = Student_course_fee.objects.filter(user=request.user).values_list('selected_course_id', flat=True)
    
    return render(request, 'enrollcourse.html', {'data': data, 'enrolled_course_ids': enrolled_course_ids})





def teacher_data(request):
    data=NewUser.objects.all().values().filter(user_type="teacher")
    
    return render(request,'teacher_data.html',{"data":data})
    
def trainers(request):
    return render(request,'trainers.html.html')
    
    
def rec_dash(request):
    data = len(Course.objects.all())
    data2 = len(NewUser.objects.all().values().filter(user_type="student"))
    data3 = len(NewUser.objects.all().values().filter(user_type="teacher"))
    
    context={'data':data,"data2":data2,"data3":data3}
    
    return render(request,'rec_dash.html',context)
    
    
def rec_students(request):
    data=NewUser.objects.all().values().filter(user_type="student")
    
    return render(request,'rec_students.html',{"data":data})
   
@login_required 
def rec_student_courses(request, student_id):
    # print("\n\n\nyes in")
    # student = NewUser.objects.get(id=student_id)
    # courses_taken = Student_course_fee.objects.filter(user=student)
    # print("Till Now\n\n\n")
    # # student_course_fee=Student_course_fee.objects.filter(student_id_id=student_id , selected_course_id_id=course_id)
    # print("\n\n\n",course_taken,"\n\n\n")
    
    # remaing_fee=courses_taken.course_fee -courses_taken.paid_amount
    
    # print("\n\n\n",remaing_fee,"\n\n\n")
    
    
 
    return render(request, 'rec_student_courses.html', {"student": student})
    # return HttpResponse("hello")


from django.shortcuts import get_object_or_404

def rec_student_course_info(request, student_id, course_id):
    
    student = get_object_or_404(NewUser, id=student_id)
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        amount_paid = request.POST.get('amount_paid')

    # Update the paid_amount field for the matching Student_course_fee object
        Student_course_fee.objects.filter(user=student, selected_course_id=course).update(paid_amount=amount_paid)

    return render(request, 'fee_update.html')

def up(request,student_id,course_id):
    
    student=get_object_or_404(NewUser, id=student_id)
    course=get_object_or_404(Course, id=course_id)
    obj=Student_course_fee.objects.get(user=student , selected_course_id=course)
    if request.method == 'POST':
        amount= request.POST['amount_paid']
      
        
        
        obj.paid_amount=int(amount)+int(obj.paid_amount)
        obj.save()
        return redirect("rec_students")
    remaining_amount=int(obj.course_fee)-int(obj.paid_amount)
   
    return render(request,'fee_update.html',{'remaining_amount':remaining_amount})
# def up(request,student_id,course_id):
    
#     student=get_object_or_404(NewUser, id=student_id)
#     course=get_object_or_404(Course, id=course_id)
#     obj=Student_course_fee.objects.get(user=student , selected_course_id=course)
#     if request.method == 'POST':
#         amount= request.POST['amount_paid']
      
        
        
#         obj.paid_amount=int(amount)+int(obj.paid_amount)
#         obj.save()
#         return redirect("rec_students")
#     remaining_amount=int(obj.course_fee)-int(obj.paid_amount)
   
#     return render(request,'fee_update.html',{'remaining_amount':remaining_amount})
    
    

@login_required
def rec_student_courses(request, student_id):
    print("\n\n\nyes in")
    student = NewUser.objects.get(id=student_id)
    courses_taken = Student_course_fee.objects.filter(user=student)
    for course_taken in courses_taken:
        remaining_fee = float(course_taken.course_fee) - float(course_taken.paid_amount)
        course_taken.remaining_fee = remaining_fee
    return render(request, 'rec_student_courses.html', {"student": student, "courses_taken": courses_taken})

def rec_student_course_fee_update(request,student_id,course_id):
    obj=Student_course_fee.objects.filter(user=student_id ,selected_course_id=course_id)
    return render(request,'fee_update.html')

@login_required
def update_course_fee(request, student_id, course_id):
    student = NewUser.objects.get(id=student_id)
    obj=Student_course_fee.objects.get(user=student, selected_course_id=course_id)
    course = Course.objects.get(id=course_id)
    print(">>>>>>>>>>>>>>>>>>>>>>>cours FEe",course.fee)
        
    if request.method == 'POST':
       
        amount_paid1 = request.POST.get('amount_paid')
        obj=Student_course_fee.objects.create(course_fee=course.fee,paid_amount=amount_paid1,user=student,selected_course_id=course_id) 
        obj.amount_paid = amount_paid1
        
        obj.save()
        print("+++++++++++++++++++saved!")
        messages.success(request, 'Course fee updated successfully.')
        
    student = NewUser.objects.get(id=student_id)
    course = Course.objects.get(id=course_id)
    return render(request, 'rec_update_fee.html', {'student': student, 'course': course})

