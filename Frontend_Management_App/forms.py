
from django import forms

from Backend_Management_App.models import Beds, Academic_Sessions, Departments


class AddStudentForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="First Name", widget=forms.TextInput(attrs={"class": "form-control"}) )
    last_name = forms.CharField(max_length=50, label="Last Name", widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(max_length=50, label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=50, label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=50, label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    registration = forms.IntegerField( widget=forms.NumberInput(attrs={"class": "form-control"}))
    adress = forms.CharField(max_length=50, label="Address", widget=forms.TextInput(attrs={"class": "form-control"}))
    
    
    session_list = []
    for session in Academic_Sessions.objects.all():
        session_template = (session.session, session.session)
        session_list.append(session_template)
    session = forms.ChoiceField( label="Academic Session", choices=session_list, widget=forms.Select(attrs={"class": "form-control"}))

    department_list = []
    for department in Departments.objects.all():
        department_template = (department.department_name, department.department_name)
        department_list.append(department_template)
    department = forms.ChoiceField( label="Department Name", choices=department_list, widget=forms.Select(attrs={"class": "form-control"}))
    

    bed_list = []
    for bed in Beds.objects.filter(status=1):
        bed_template = (bed.bed_name, bed.bed_name)
        bed_list.append(bed_template)
    bed_name = forms.ChoiceField( label="Bed Number", choices=bed_list, widget=forms.Select(attrs={"class": "form-control"}))

    profile_pic = forms.FileField(label="Profile Pic", widget=forms.FileInput(attrs={"class": "form-control"}))
    
    
#*************************************EditStudentForm***********************************************************
class EditStudentForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="First Name", widget=forms.TextInput(attrs={"class": "form-control"}) )
    last_name = forms.CharField(max_length=50, label="Last Name", widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(max_length=50, label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=50, label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    registration = forms.IntegerField( widget=forms.NumberInput(attrs={"class": "form-control"}))
    adress = forms.CharField(max_length=50, label="Address", widget=forms.TextInput(attrs={"class": "form-control"}))
    
    
    session_list = []
    for session in Academic_Sessions.objects.all():
        session_template = (session.id, session.session)
        session_list.append(session_template)
    session = forms.ChoiceField( label="Academic Session", choices=session_list, widget=forms.Select(attrs={"class": "form-control"}))

    department_list = []
    for department in Departments.objects.all():
        department_template = (department.id, department.department_name)
        department_list.append(department_template)
    department = forms.ChoiceField( label="Department Name", choices=department_list, widget=forms.Select(attrs={"class": "form-control"}))
    
    
    def __init__(self, *args, **kwargs):
        bed_name = kwargs.pop('bed', None)
        bed_list = kwargs.pop('bed_list', None)
        super().__init__(*args, **kwargs)
        self.fields['bed_name'].choices = bed_list
        self.fields['bed_name'].initial = bed_name
    beds = Beds.objects.filter(status=1)
    bed_list = []
    for bed in beds:
        bed_template = (bed.bed_name, bed.bed_name)
        bed_list.append(bed_template)
    bed_name = forms.ChoiceField( label="Bed Number", choices=bed_list, widget=forms.Select(attrs={"class": "form-control"}))
    
    profile_pic = forms.FileField(label="Profile Pic", widget=forms.FileInput(attrs={"class": "form-control"}), required=False)
    
