
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('mainindex', views.mainindex, name="mainindex"),
    path('profile', views.profile, name="profile"),
    path('trainer', views.trainer, name="trainer"),
    path('courses', views.courses, name="courses"),
    path('login', views.handellogin, name="login"),
    path('handellogout', views.handellogout, name="handellogout"),
    path('register', views.register, name="register"),
    path('dash', views.dash, name="dash"),
    path('addcourse', views.addcourse, name="addcourse"),
    path('addteacher', views.addteacher, name="addteacher"),
    path('allcourse', views.allcourse, name="allcourse"),
    path('student', views.student, name="student"),
    path('teacher', views.teacher, name="teacher"),
    path('studentcourse', views.studentcourse, name="studentcourse"),
]
