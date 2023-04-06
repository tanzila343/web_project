from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import RequestContext
from django.shortcuts import render, redirect
from Backend_Management_App.forms import AddStudentForm, EditStudentForm
from Backend_Management_App.models import CustomUser, Beds, Students, Academic_Sessions, Departments
from django.views.decorators.csrf import csrf_exempt


def addStudent(request):
    form  = AddStudentForm()
    return render(request, 'student_template/add_student_template.html', {"form": form})


def addStudentSave(request):
    if request.method == "POST":
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            adress = form.cleaned_data['adress']
            registration = form.cleaned_data['registration']
            session = form.cleaned_data['session']
            department = form.cleaned_data['department']
            bed_name = form.cleaned_data['bed_name']

            profile_pic = request.FILES.get('profile_pic', False)
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                    last_name=last_name, first_name=first_name, user_type=3)
                user.students.adress = adress
                user.students.registration = registration
                user.students.session = Academic_Sessions.objects.get(session=session)
                user.students.department = Departments.objects.get(department_name=department)
                user.students.profile_pic = profile_pic_url
                user.students.bed = Beds.objects.get(bed_name=bed_name)
                Beds.objects.filter(bed_name=bed_name).update(status=2)
                user.save()
                
                messages.success(request, "Successfully Added Student")
                return HttpResponseRedirect(reverse("add_student"))
            except:
                messages.error(request, "Can't Added Student exception")
                return HttpResponseRedirect(reverse("add_student"))
    else:
        messages.error(request, "Can't Added Student else")
        return HttpResponseRedirect(reverse("add_student"))



def manageStudent(request):
    students = Students.objects.all()
    for student in students:
        student.room_number = student.bed.room.room_number
        student.save()
    return render(request, 'student_template/manage_student_template.html', {"students": students})


def deleteStudent(request, student_id):
    try:
        cu = CustomUser.objects.get(id=student_id)
        cu.delete()
        messages.success(request, "The student has been deleted")
        
    except student_id.DoesNotExist:
        messages.success(request, "The student does not exist")
    
    return redirect('/manage_student/')


def editStudent(request, student_id):
    student = Students.objects.get(admin=student_id)
    Beds.objects.filter(bed_name=student.bed.bed_name).update(status=1)
    beds = Beds.objects.filter(status=1)
    departments = Departments.objects.all()
    sessions = Academic_Sessions.objects.all()
    return render(request, 'student_template/edit_student_template.html', {"beds":beds, "departments":departments, "sessions":sessions ,"student":student})


def editStudentSave(request):
    if request.method == "POST":   
        student_id = request.POST.get('student_id')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email'] 
        adress = request.POST['adress']
        registration = request.POST['registration']
        session = request.POST['session']
        department = request.POST['department']
        bed_name = request.POST['bed_name']
        
        if request.FILES.get('profile_pic', False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None
        try:
            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

            students = Students.objects.get(admin=student_id)
            students.adress = adress
            students.department = Departments.objects.get(id=department)
            students.session = Academic_Sessions.objects.get(id=session)
            students.registration = registration
            students.bed_name = Beds.objects.get(bed_name=bed_name)
            Beds.objects.filter(bed_name=bed_name).update(status=2)
            if profile_pic_url != None:
                students.profile_pic = profile_pic_url
            students.save()
            
            messages.success(request, "Successfully Edited Student")
            return HttpResponseRedirect(reverse('manage_student'))
        except:
            editStudent(student_id)
    else:
        return HttpResponse("Method not allowed")




"""
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Backend_Management_App.models import CustomUser, Departments, Academic_Sessions, Beds, Students
from Backend_Management_App.forms import *


class StudentListView(LoginRequiredMixin, ListView):
    model = Students
    template_name = 'student_template/manage_student_template.html'
    context_object_name = 'students'
    login_url = '/login/'


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    model = Students
    template_name = 'student_template/add_student_template.html'
    form_class = AddStudentForm
    success_url = reverse_lazy('manage_student')
    login_url = '/login/'


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Students
    template_name = 'student_template/edit_student_template.html'
    form_class = EditStudentForm
    success_url = reverse_lazy('manage_student')
    login_url = '/login/'

    def get_initial(self):
        student = self.get_object()
        Beds.objects.filter(id=student.bed).update(status=1)
        available_beds = Beds.objects.filter(status=1)
        bed_list = [(bed.bed_name, bed.bed_name) for bed in available_beds]
        initial_data = {
            'first_name': student.admin.first_name,
            'last_name': student.admin.last_name,
            'username': student.admin.username,
            'email': student.admin.email,
            'registration': student.registration,
            'department': student.department,
            'session': student.session,
            'adress': student.adress,
            'bed_name': student.bed_name
        }
        return initial_data,bed_list


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Students
    #template_name = 'student_template/delete_student_template.html'
    success_url = reverse_lazy('manage_student')
    login_url = '/login/'
"""