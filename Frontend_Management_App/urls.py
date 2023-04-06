from django.urls import path
from . import views
from .views import NoticeListView

urlpatterns = [
    path('', NoticeListView.as_view(), name="home"),
    #path('home/', views.HomePage, name="home"),
    path('home/', NoticeListView.as_view(), name="home"),
    path('about/', views.AboutPage, name="about"),
    path('student/', views.StudentPage, name="student"),
    path('student_info/', views.StudentInfoPage, name="student_info"),
    path('provost/', views.ProvostPage, name="provost"),
    path('Department_info/', views.DepartmentInfoPage, name="Department_info"),
    path('service/', views.ServicePage, name="service"),
    path('provost_service/', views.ProvostServicePage, name="provost_service"),
    path('stuff_service/', views.StuffPage, name="stuff_service"),
    path('contact/', views.ContactPage, name="contact"),
    path('student_registration/', views.registerStudent, name="student_registration"),
    path('new_student_save/', views.registerStudentSave, name="new_student_save"),
    #path('media/', views.media_serve, name='media_serve'),
]
