from rest_framework import serializers
from Backend_Management_App.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields  = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields  = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields  = '__all__'


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beds
        fields  = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Departments
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        models = Academic_Sessions
        fields = '__all__'
    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields  = '__all__'