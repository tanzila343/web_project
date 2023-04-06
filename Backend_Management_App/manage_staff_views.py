# from django.contrib import messages
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from Backend_Management_App.models import Staffs, CustomUser



# *******************  STAFF MANAGE  *****************
def addStaff(request):
    return render(request, 'staff_template/add_staff_template.html')


def addStaffSave(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=2)
            user.save()
            
            messages.success(request, "Successfully Added Staff")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request, "Staff Add Unsuccessful")
            return HttpResponseRedirect(reverse("add_staff"))
    else:
        messages.error(request, "Method not allowed")
        return HttpResponseRedirect(reverse("add_staff"))


def manageStaff(request):
    staffs = Staffs.objects.all()
    return render(request, 'staff_template/manage_staff_template.html', {"staffs": staffs})


def deleteStaff(request, staff_id):
    try:
        #staffs = Staffs.objects.get(admin=staff_id)
        cu = CustomUser.objects.get(id=staff_id)
        #staffs.delete();
        cu.delete()
        messages.success(request, "The staff has been deleted")
        
    except staff_id.DoesNotExist:
        messages.success(request, "The staff does not exist")
    
    return redirect('/manage_staff/')


def editStaff(request, staff_id):
    staffs = Staffs.objects.get(admin=staff_id)
    return render(request, 'staff_template/edit_staff_template.html', {"staffs": staffs, "id": staff_id})


def editStaffSave(request):
    if request.method == "POST":
        staff_id = request.POST['staff_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']

        user = CustomUser.objects.get(id=staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()
        messages.success(request, "Successfully Edited Staff")
        return HttpResponseRedirect(reverse("manage_staff"))
    else:
        messages.error(request, "Unsuccessfull")
        return HttpResponseRedirect(reverse("manage_staff"))










"""
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Backend_Management_App.models import Staffs

class StaffListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'staff_template/manage_staff_template.html'
    context_object_name = 'staffs'
    login_url = '/login/'

class StaffCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    fields = ('first_name', 'last_name', 'username', 'email', 'password', 'user_type=2')
    template_name = 'staff_template/add_staff_template.html'
    success_url = reverse_lazy('add_staff')
    login_url = '/login/'

class StaffUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ('first_name', 'last_name', 'username', 'email')
    template_name = 'staff_template/edit_staff_template.html'
    success_url = reverse_lazy('manage_staff')
    login_url = '/login/'

class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = Staffs
    template_name = 'staff_template/delete_staff_template.html'
    success_url = reverse_lazy('manage_staff')
"""
"""
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator


from Backend_Management_App.models import CustomUser, Rooms, Beds, Staffs

def is_admin(user):
    return user.user_type == "ADMIN"

class AdminHomeView(ListView):
    template_name = 'staff_template/home_content.html'
    context_object_name = 'admin'
    model = CustomUser

    def get_queryset(self):
        return CustomUser.objects.filter(user_type='ADMIN')

    @method_decorator(login_required(login_url='/login/'))
    @method_decorator(user_passes_test(is_admin))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class StaffListView(ListView):
    template_name = 'staff_template/manage_staff_template.html'
    context_object_name = 'staffs'
    model = Staffs

    @method_decorator(login_required(login_url='/login/'))
    @method_decorator(user_passes_test(is_admin))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class StaffCreateView(CreateView):
    template_name = 'staff_template/add_staff_template.html'
    model = Staffs
    fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def form_valid(self, form):
        form.instance.user_type = "STAFF"
        messages.success(self.request, "Successfully Added Staff")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Staff Add Unsuccessful")
        return super().form_invalid(form)

    @method_decorator(login_required(login_url='/login/'))
    @method_decorator(user_passes_test(is_admin))
    def dispatch(self, *args, **kwargs):
        return super
"""
