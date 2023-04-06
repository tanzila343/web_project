
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    user_type_data = ((1, "ADMIN"), (2, "STAFF"), (3, "STUDENT"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=20)


class Admin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    objects = models.Manager()


class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager()


class Rooms(models.Model):
    room_number = models.IntegerField(primary_key=True) 
    room_capacity = models.IntegerField(null=True) 
    bed_avilable = models.IntegerField(null=True) 
    staff = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager()
    
    def __str__(self):
        return self.room_number


class Beds(models.Model):
    bed_name = models.CharField(max_length=50, primary_key=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    status_data = ((1, "AVILABLE"), (2, "BOOKED"), (3, "PROCESSING"))
    status = models.CharField(default=1, choices=status_data, max_length=20)
    objects = models.Manager()

    def __str__(self):
        return self.bed_name
        

class Departments(models.Model):
    department_name = models.CharField(max_length=50, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.department_name


class Academic_Sessions(models.Model):
    session = models.CharField(max_length=50, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.session


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    registration = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(Academic_Sessions, on_delete=models.CASCADE, null=True)
    adress = models.CharField(max_length=100)
    room_number = models.CharField(max_length=20,null=True)
    bed = models.ForeignKey(Beds, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.registration


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Rooms, on_delete=models.DO_NOTHING)
    attendence_date = models.DateField()
    objects = models.Manager()
    def __str__(self):
        return self.id

class AttendanceReport(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    attendence = models.ForeignKey(Attendance, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)
    objects = models.Manager()
    def __str__(self):
        return self.id


class FeedBackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback = models.TextField(null=True)
    feedback_reply = models.TextField(null=True)
    objects = models.Manager()


class FeedBackStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    feedback = models.TextField(null=True)
    feedback_reply = models.TextField(null=True)
    objects = models.Manager()


class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    objects = models.Manager()

    
class NotificationStaff(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    objects = models.Manager()


class Notice(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()
    notice_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.heading



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        """if instance.user_type == 3:
            Students.objects.create(admin=instance, adress="adress", profile_pic="profile_pic", registration="registration",)
        """

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.staffs.save()
    """ if instance.user_type == 3:
        instance.students.save()"""

"""@receiver(post_save, sender=Students)
def create_custom_user(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user_type=3, username=instance.username, password=instance.password,
                                   email=instance.email, first_name=instance.first_name, last_name=instance.last_name)
"""