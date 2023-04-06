
# from django.contrib import messages
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Backend_Management_App.models import  * 
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='/login/')
def admin_home(request):
    if request.user is not None:
        return render(request, 'admin_template/home_content.html')
    

def viewAttendence(request):
    rooms = Rooms.objects.all()
    return render(request, "admin_template/student_view_attendence.html", {'rooms': rooms})

def getAttendence(request):
    room_number = request.POST.get('room_number')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    
    start_date_parse = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date_parse = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    room_obj = Rooms.objects.get(room_number=room_number)
    
    attendence = Attendance.objects.filter(attendence_date__range = (start_date_parse, end_date_parse), room=room_obj)
    attendence_report = AttendanceReport.objects.filter(attendence__in=attendence)
    
    return render(request, "admin_template/student_attendence_data.html", {'attendence_report': attendence_report})






def studentFeedbackMessage(request):
    feedbacks = FeedBackStudent.objects.all()
    return render(request, 'admin_template/student_feedback_message.html', {"feedbacks": feedbacks})

@csrf_exempt
def studentFeedbackMessageReply(request):
    id = request.POST.get('id')
    message = request.POST.get('message')
    try:
        feedback = FeedBackStudent.objects.get(id=id)
        feedback.feedback_reply = message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")


def staffFeedbackMessage(request):
    feedbacks = FeedBackStaff.objects.all()
    return render(request, 'admin_template/staff_feedback_message.html', {"feedbacks": feedbacks})

@csrf_exempt
def staffFeedbackMessageReply(request):
    id = request.POST.get('id')
    message = request.POST.get('message')
    try:
        feedback = FeedBackStaff.objects.get(id=id)
        feedback.feedback_reply = message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

from .models import Notice
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class NoticeListView(ListView):
    model = Notice
    template_name = 'admin_template/notice.html'
    context_object_name = 'notices'
    ordering = ['-notice_date']


class NoticeCreateView(CreateView):
    model = Notice
    fields = ['heading', 'description']
    template_name = 'admin_template/notice_form.html'
    success_url = reverse_lazy('notice_list')


class NoticeUpdateView(UpdateView):
    model = Notice
    fields = ['heading', 'description']
    template_name = 'admin_template/notice_form.html'
    success_url = reverse_lazy('notice_list')


class NoticeDeleteView(DeleteView):
    model = Notice
    template_name = 'admin_template/notice_confirm_delete.html'
    success_url = reverse_lazy('notice_list')



@csrf_exempt
def checkEmail(request):
    email = request.POST.get('email')
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
    
@csrf_exempt
def checkUsername(request):
    username = request.POST.get('username')
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
    
@csrf_exempt
def checkRegistration(request):
    registration = request.POST.get('registration')
    user_obj = Students.objects.filter(registration=registration).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

