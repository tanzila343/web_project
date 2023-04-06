from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Backend_Management_App.models import  Departments, Academic_Sessions
from django.contrib.messages.views import SuccessMessageMixin


#******************** Department ****************
class DepartmentListView(ListView):
    model = Departments
    template_name = 'dept_session_template/manage_department_template.html'
    context_object_name = 'departments'


class DepartmentCreateView(SuccessMessageMixin, CreateView):
    model = Departments
    fields = ('department_name',)
    template_name = 'dept_session_template/add_department_template.html'
    success_message = 'Successfully Added Department'
    success_url = reverse_lazy('manage_department')


class DepartmentDeleteView(SuccessMessageMixin, DeleteView):
    model = Departments
    success_message = 'Successfully Deleted Department'
    success_url = reverse_lazy('manage_department')


#******************** Academic_Sessions ****************
class Academic_SessionListView(ListView):
    model = Academic_Sessions
    template_name = 'dept_session_template/manage_session_template.html'
    context_object_name = 'sessions'


class Academic_SessionCreateView(SuccessMessageMixin, CreateView):
    model = Academic_Sessions
    fields = ('session',)
    template_name = 'dept_session_template/add_session_template.html'
    success_message = 'Successfully Added Academic_Session'
    success_url = reverse_lazy('manage_session')


class Academic_SessionDeleteView(SuccessMessageMixin, DeleteView):
    model = Academic_Sessions
    success_message = 'Successfully Deleted Academic_Session'
    success_url = reverse_lazy('manage_session')
