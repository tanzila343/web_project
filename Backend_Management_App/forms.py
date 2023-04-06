
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
    


"""
from django import forms
from Backend_Management_App.models import CustomUser, Staffs, Rooms, Beds, Students

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staffs
        fields = ('admin',)

class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ('room_name', 'room_capacity')

class BedForm(forms.ModelForm):
    class Meta:
        model = Beds
        fields = ('bed_name', 'room', 'status')

"""
"""
#class StudentForm(forms.ModelForm):
#    class Meta:
#        model = Students
#        fields = ('admin', 'registration', 'department', 'session', 'adress', 'bed', 'profile_pic')
"""
"""
class AddStudentForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    registration = forms.CharField(max_length=255)
    department = forms.CharField(max_length=255)
    session = forms.CharField(max_length=255)
    adress = forms.CharField(max_length=255)
    bed_name = forms.ChoiceField(choices=[(bed.bed_name, bed.bed_name) for bed in Beds.objects.all()])
    profile_pic = forms.ImageField()
    password = forms.CharField(widget=forms.PasswordInput)

class EditStudentForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    registration = forms.CharField(max_length=255)
    department = forms.CharField(max_length=255)
    session = forms.CharField(max_length=255)
    adress = forms.CharField(max_length=255)
    bed_name = forms.ChoiceField()
    profile_pic = forms.ImageField()
    
    def __init__(self, *args, **kwargs):
        bed_list = kwargs.pop('bed_list', None)
        super(EditStudentForm, self).__init__(*args, **kwargs)
        self.fields['bed_name'].choices = bed_list

"""

"""
from django import forms
from Backend_Management_App.models import CustomUser, Students, Beds,Departments, Academic_Sessions

class AddStudentForm(forms.ModelForm):
    bed_name = forms.ModelChoiceField(queryset=Beds.objects.filter(status=1), empty_label="Select a bed")
    department = forms.ModelChoiceField(queryset=Departments.objects.all(), empty_label="Department")
    session = forms.ModelChoiceField(queryset=Academic_Sessions.objects.all(), empty_label="Session")
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password', ]
        model = Students
        fields = [ 'registration', 'department', 'session', 'adress', 'bed_name', 'profile_pic']

class EditStudentForm(forms.ModelForm):
    bed_name = forms.ModelChoiceField(queryset=Beds.objects.all(), empty_label="Select a bed")
    class Meta:
        model = Students
        fields = ['first_name', 'last_name', 'username', 'email', 'registration', 'department', 'session', 'adress', 'bed_name', 'profile_pic']

"""