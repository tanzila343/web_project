import json
from django.contrib import messages
from django.shortcuts import render
from Backend_Management_App.models import * #Rooms, Students, Attendance, AttendanceReport, Staffs
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse


def staffHome(request):
    return render(request, "staff_view_template/staff_home.html")


def staffTakeAttendence(request):
    rooms = Rooms.objects.filter(staff = request.user.id)
    return render(request, "staff_view_template/staff_take_attendence.html", {"rooms": rooms})

@csrf_exempt
def getStudents(request):
    room_number = request.POST['room_number']
    students = Students.objects.filter(room_number=room_number)

    list_data=[]
    for student in students:
        data_small = {"id": student.admin.id, "name": student.admin.first_name+" "+ student.admin.last_name}
        list_data.append(data_small)    
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@csrf_exempt
def saveAttendenceData(request):
    students_id = request.POST.get("students_id")
    attendence_date = request.POST.get("attendence_date")
    room_number = request.POST.get("room_number")
    try:
        attendence = Attendance(room=Rooms.objects.get(room_number=room_number), attendence_date=attendence_date)
        attendence.save()
        student_data = json.loads(students_id)
        for std in student_data:
            student = Students.objects.get(admin=std['id'])
            print(student)
            attendence_report = AttendanceReport(student=student, status=std['status'], attendence=attendence)
            attendence_report.save()
            
        return HttpResponse("OK")
    except:
        return HttpResponse("ERROR")
    
        
def staffUpdateAttendence(request):
    rooms = Rooms.objects.filter(staff = request.user.id)
    return render(request, "staff_view_template/staff_update_attendence.html", {"rooms": rooms})

@csrf_exempt
def getAttendenceDates(request):
    room_number = request.POST.get('room_number')
    attendence = Attendance.objects.filter(room=room_number)
    list_data = []
    for data in attendence:
        data_small = {"id": data.id, "attendence_date": str(data.attendence_date)}
        list_data.append(data_small)    
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)

@csrf_exempt
def getAttendenceStudents(request):
    attendence_date = request.POST.get('attendence_date')
    attendence = Attendance.objects.get(id=attendence_date)
    attendence_data = AttendanceReport.objects.filter(attendence=attendence)
    list_data = []
    for data in attendence_data:
        data_small = {"id": data.student.admin.id, "name": data.student.admin.first_name+" "+ data.student.admin.last_name, "status":data.status}
        list_data.append(data_small)    
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@csrf_exempt
def saveUpdateAttendenceData(request):
    students_id = request.POST.get("students_id")
    attendence_date = request.POST.get("attendence_date")
    
    attendence = Attendance.objects.get(id=attendence_date)
    try:
        
        student_data = json.loads(students_id)
        for std in student_data:
            student = Students.objects.get(admin=std['id'])
            print(student)
            attendence_report = AttendanceReport.objects.get(student=student, attendence=attendence)
            attendence_report.status=std['status']
            attendence_report.save()   
        return HttpResponse("OK")
    except:
        return HttpResponse("ERROR")
    

def staffFeedback(request):
    staff = Staffs.objects.get(admin=request.user.id)
    feedback = FeedBackStaff.objects.filter(staff=staff)
    return render(request, "staff_view_template/staff_feedback.html", {"feedback": feedback})


def saveStaffFeedback(request):
    if request.method == "POST":
        feedback_msg = request.POST.get("feedback_msg")
        staff = Staffs.objects.get(admin = request.user.id)
        try:
            feedback_obj = FeedBackStaff(staff=staff, feedback=feedback_msg, feedback_reply="")
            feedback_obj.save()
            messages.success(request, "Successfully Send feedback message")
            return HttpResponseRedirect(reverse("staff_feedback"))
        except:
            messages.error(request, "Failed to Send feedback message")
            return HttpResponseRedirect(reverse("staff_feedback"))
    else:
        messages.error(request, "Failed to feedback !!!")
        return HttpResponseRedirect(reverse("staff_feedback"))
    