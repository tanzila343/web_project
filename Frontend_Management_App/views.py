from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from Frontend_Management_App.forms import AddStudentForm, EditStudentForm
from Backend_Management_App.models import CustomUser, Beds, Students, Academic_Sessions, Departments
from django.views.static import serve


# Create your views here.


"""def HomePage(request):
    return render(request, 'frontend/notice.html')

"""
def DepartmentInfoPage(request):
    return render(request, 'frontend/Department_info.html')
def ProvostServicePage(request):
    return render(request, 'frontend/provost_service.html')
def ProvostPage(request):
    return render(request, 'frontend/provost.html')
def StudentInfoPage(request):
    return render(request, 'frontend/student_info.html')
def StudentPage(request):
    return render(request, 'frontend/student.html')
def StuffPage(request):
    return render(request, 'frontend/stuff_service.html')
def AboutPage(request):
    return render(request, 'frontend/About.html')


def ContactPage(request):
    return render(request, 'frontend/contact.html')


def ServicePage(request):
    return render(request, 'frontend/service.html')


def registerStudent(request):
    form  = AddStudentForm()
    return render(request, 'frontend/student_registration.html', {"form": form})


def registerStudentSave(request):
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
            #try:

            user = CustomUser(username=username,email=email,last_name=last_name, first_name=first_name, user_type=3)
            user.set_password(password)
            user.save()
                
            id = user.id
            student = Students( adress = adress, registration = registration, session = Academic_Sessions.objects.get(session=session),
                            department = Departments.objects.get(department_name=department), profile_pic = profile_pic_url,
                            bed = Beds.objects.get(bed_name=bed_name), admin=user)
            Beds.objects.filter(bed_name=bed_name).update(status=2)

            student.save()

            form  = AddStudentForm()
            return render(request, 'frontend/student_registration.html', {"form": form}) 
            #except:
                #messages.error(request, "Can't Added Student exception")
                #return HttpResponseRedirect(reverse("student_registration"))
    else:
        messages.error(request, "Can't Added Student else")
        return HttpResponseRedirect(reverse("student_registration"))


from Backend_Management_App.models import Notice
from django.views.generic import ListView
from django.contrib.auth.decorators import user_passes_test


"""def allow_unauthenticated(user):
    return not user.is_authenticated"""

class NoticeListView(ListView):
    model = Notice
    template_name = 'frontend/notice.html'
    context_object_name = 'notices'
    ordering = ['-notice_date']
    paginate_by = 3
"""
    @user_passes_test(allow_unauthenticated)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)"""