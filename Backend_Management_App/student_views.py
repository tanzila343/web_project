
import json
import datetime
from django.contrib import messages
from django.shortcuts import render
from Backend_Management_App.models import * 
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse

def studentHome(request):
    return render(request, "student_view_template/student_home.html")


def studentViewAttendence(request):
    student = Students.objects.get(admin = request.user.id)
    rooms = Rooms.objects.get(room_number = student.room_number)
    return render(request, "student_view_template/student_view_attendence.html", {'rooms': rooms})

def studentGetAttendence(request):
    room_number = request.POST.get('room_number')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    
    start_date_parse = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date_parse = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    room_obj = Rooms.objects.get(room_number=room_number)
    user_obj = CustomUser.objects.get(id = request.user.id)
    std_obj = Students.objects.get(admin = user_obj)
    attendence = Attendance.objects.filter(attendence_date__range = (start_date_parse, end_date_parse), room=room_obj)
    attendence_report = AttendanceReport.objects.filter(attendence__in=attendence, student=std_obj)
    
    return render(request, "student_view_template/student_attendence_data.html", {'attendence_report': attendence_report})



def studentFeedback(request):
    student = Students.objects.get(admin=request.user.id)
    feedback = FeedBackStudent.objects.filter(student=student)
    return render(request, "student_view_template/student_feedback.html", {"feedback": feedback})


def saveStudentFeedback(request):
    if request.method == "POST":
        feedback_msg = request.POST.get("feedback_msg")
        student = Students.objects.get(admin = request.user.id)
        try:
            feedback_obj = FeedBackStudent(student=student, feedback=feedback_msg, feedback_reply="")
            feedback_obj.save()
            messages.success(request, "Successfully Send feedback message")
            return HttpResponseRedirect(reverse("student_feedback"))
        except:
            messages.error(request, "Failed to Send feedback message")
            return HttpResponseRedirect(reverse("student_feedback"))
    else:
        messages.error(request, "Failed to feedback !!!")
        return HttpResponseRedirect(reverse("student_feedback"))
    

def profile_view(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        'profile_pic': user.students.profile_pic,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
        'address': user.students.adress,
        'registration': user.students.registration,
        'session': user.students.session,
        'department': user.students.department,
        'room_number': user.students.room_number,
        'bed_name': user.students.bed,
    }
    return render(request, 'student_view_template/profile.html', context=context)