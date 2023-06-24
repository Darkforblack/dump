
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('mainindex', views.mainindex, name="mainindex"),
    path('mainindex2', views.mainindex2, name="mainindex2"),
    path('profile', views.profile, name="profile"),
    path('pro_student', views.pro_student, name="pro_student"),
    path('courses', views.courses, name="courses"),
    path('login', views.handellogin, name="login"),
    path('handellogout', views.handellogout, name="handellogout"),
    path('register/', views.register, name="register"),
    path('dash', views.dash, name="dash"),
    path('addcourse', views.addcourse, name="addcourse"),
    path('update_course/<int:course_id>/', views.update_course, name='update_course'),
    path('addteacher', views.addteacher, name="addteacher"),
    path('allcourse', views.allcourse, name="allcourse"),
    path('student', views.student, name="student"),
    path('teachers', views.teacher, name="teachers"),
    path('teacher_data/', views.teacher_data, name="teacher_data"),
    path('studentcourse', views.studentcourse, name="studentcourse"),
    path('import_data', views.import_data, name="import_data"),
    path('studentcourse', views.studentcourse, name="studentcourse"),
    path('enrollcourse', views.enrollcourse, name="enrollcourse"),
    path('rec_dash', views.rec_dash, name="rec_dash"),
    path('rec_students', views.rec_students, name="rec_students"),
    path('course_taken', views.course_taken, name="course_taken"),
    path('update_course_fee/<int:student_id>', views.update_course_fee, name='update_course_fee'),
    path('rec_student_courses/<int:student_id>/', views.rec_student_courses, name='rec_student_courses'),
    path('rec_student_course_info/<int:student_id>/<int:course_id>/', views.rec_student_course_info, name='rec_student_course_info'),
    path('rec_student_course_fee_update/<int:student_id>/<int:course_id>/', views.rec_student_course_fee_update, name='rec_student_course_fee_update'),
    path('up/<int:student_id>/<int:course_id>/', views.up, name='up'),
    path('remove_user/<int:student_id>/', views.remove_user, name='remove_user'),

]
