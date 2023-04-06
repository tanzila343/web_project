
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from Backend_Management_App.EmailBackEnd import EmailBackEnd


def BackendController(request):
    return render(request, 'admin_template/index.html')


def LoginPage(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request, username=request.POST["email"],
                                         password=request.POST["password"])
        print(user)
        if user is not None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            return HttpResponse('Invalid Details')
    else:
        return HttpResponse("<h2>NOT ALLOWED</h2>")


@login_required(login_url='/login/')
def GetUserDetails(request):
    if request.user is not None:
        return HttpResponse("User : " + request.user.email + "Usertype : " + request.user.user_type)
    else:
        return HttpResponse("Please Login first")


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    request.session.flush()
    return redirect('home')
















"""def is_admin(user):
    return user.user_type == "ADMIN"

class AdminHomeView(ListView):
    template_name = 'backend/admin_template/home_content.html'
    context_object_name = 'admin'
    model = CustomUser

    def get_queryset(self):
        return CustomUser.objects.filter(user_type='ADMIN')

    @method_decorator(login_required(login_url='/login/'))
    @method_decorator(user_passes_test(is_admin))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class StaffListView(ListView):
    template_name = 'backend/admin_template/manage_staff_template.html'
    context_object_name = 'staffs'
    model = Staffs

    @method_decorator(login_required(login_url='/login/'))
    @method_decorator(user_passes_test(is_admin))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class StaffCreateView(CreateView):
    template_name = 'backend/admin_template/add_staff_template.html'
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