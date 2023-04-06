# from django.contrib import messages
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from Backend_Management_App.models import Rooms, Beds, Staffs, CustomUser


# *******************  ROOM MANAGE  *****************
def addRoom(request):
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request, 'room_template/add_room_template.html', {"staffs": staffs})


def addRoomSave(request):
    if request.method != "POST":
        messages.error(request, "Method not allowed")
        return HttpResponseRedirect(reverse("add_room"))
    else:
        room_number = request.POST['room_number']
        id = request.POST['staff']
        
        try:
            Rooms(room_number=room_number,
                   staff=CustomUser.objects.get(id=id)).save()
            messages.success(request, "Successfully Added room")
            return HttpResponseRedirect(reverse("add_room"))
        except:
            messages.error(request, "Room Add Unsuccessful")
            return HttpResponseRedirect(reverse("add_room"))


def manageRoom(request):
    rooms = Rooms.objects.all()
    for room in rooms:
        room.room_capacity = Beds.objects.filter(room=room).count()
        beds_in_room = Beds.objects.filter(room=room)
        room.bed_avilable = beds_in_room.filter(status=1).count()
        room.save()
        
    return render(request, 'room_template/manage_room_template.html', {"rooms": rooms })


def deleteRoom(request, room_number):
    try:
        rooms = Rooms.objects.get(room_number=room_number)
        beds_in_room = Beds.objects.filter(room=room_number)
        for bed in beds_in_room:
            bed.delete()
        rooms.delete()
        messages.success(request, "The room has been deleted")
        
    except:
        messages.success(request, "The room does not exist")
    
    return redirect('/manage_room/')


def editRoom(request, room_number):
    rooms = Rooms.objects.get(room_number=room_number)
    return render(request, 'room_template/edit_room_template.html', {"rooms": rooms, "room_number": room_number})


def editRoomSave(request):
    if request.method == "POST":
        room_number = request.POST['room_number']

        room = Rooms.objects.get(room_number=room_number)
        room.save()
        messages.success(request, "Successfully Added room")
        return HttpResponseRedirect(reverse("manage_room"))
    else:
        messages.error(request, "Method not allowed")
        return HttpResponseRedirect(reverse("manage_room"))


# *******************  BED MANAGE  *****************
def addBed(request):
    rooms = Rooms.objects.all()
    return render(request, 'bed_template/add_bed_template.html', {"rooms": rooms})


def addBedSave(request):
    if request.method == "POST":
        room_number = request.POST['room_number']
        bed_name = request.POST['bed_name']

        try:
            bed_model = Beds(bed_name=bed_name, room=Rooms.objects.get(room_number=room_number))
            bed_model.save()
            messages.success(request, "Successfully Added bed")
            return HttpResponseRedirect(reverse("add_bed"))
        except:
            messages.error(request, "Bed Add Unsuccessful")
            return HttpResponseRedirect(reverse("add_bed"))
    else:
        messages.error(request, "Method not allowed")
        return HttpResponseRedirect(reverse("add_bed"))


def manageBed(request):
    beds = Beds.objects.all()
    return render(request, 'bed_template/manage_bed_template.html', {"beds": beds})


def deleteBed(request, bed_name):
    try:
        beds = Beds.objects.get(bed_name=bed_name)
        beds.delete()
        messages.success(request, "The bed has been deleted")
        
    except bed_name.DoesNotExist:
        messages.success(request, "The bed does not exist")
    
    return redirect('/manage_bed/')


def editBed(request, bed_name):
    beds = Beds.objects.get(bed_name=bed_name)
    rooms = Rooms.objects.all()
    return render(request, 'bed_template/edit_bed_template.html', {"beds": beds, "rooms": rooms, "bed_name": bed_name})


def editBedSave(request):
    if request.method == "POST":
        room_number = request.POST['room_number']
        bed_name = request.POST['bed_name']

        bed = Beds.objects.get(bed_name=bed_name)
        bed.save()
        messages.success(request, "Successfully Added bed")
        return HttpResponseRedirect(reverse("add_bed"))
    else:
        messages.error(request, "Method not allowed")
        return HttpResponseRedirect(reverse("manage_bed"))


# *******************  ... MANAGE  *****************













"""from Backend_Management_App.models import *
from Backend_Management_App.serializer import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BedList(APIView):

    def get(self, request, format=None):
        Beds = Beds.objects.all()
        serializer = BedSerializer(Beds, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = BedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BedDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Beds.objects.get(pk=pk)
        except Beds.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        Bed = self.get_object(pk)
        serializer = BedSerializer(Bed)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Bed = self.get_object(pk)
        serializer = BedSerializer(Bed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Bed = self.get_object(pk)
        Bed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""

"""from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Backend_Management_App.models import CustomUser, Rooms, Beds, Staffs

class RoomListView(ListView):
    model = Rooms
    # To access all beds in a room
    #room = Rooms.objects.get(id=1)
    #beds = room.beds_set.all()

    template_name = 'room_template/manage_room_template.html'
    context_object_name = 'rooms'

class RoomCreateView(CreateView):
    model = Rooms
    fields = ('room_name',)
    template_name = 'room_template/add_room_template.html'
    success_url = reverse_lazy('manage_room')

class RoomUpdateView(UpdateView):
    model = Rooms
    fields = ('room_name',)
    template_name = 'room_template/edit_room_template.html'
    success_url = reverse_lazy('manage_room')

class RoomDeleteView(DeleteView):
    model = Rooms
    #template_name = 'bed_template/delete_room_template.html'
    success_url = reverse_lazy('manage_room')

class BedListView(ListView):
    model = Beds
    template_name = 'bed_template/manage_bed_template.html'
    context_object_name = 'beds'

class BedCreateView(CreateView):
    model = Beds
    fields = ('bed_name', 'avilable_total', 'status', 'room_num',)
    template_name = 'bed_template/add_bed_template.html'
    success_url = reverse_lazy('manage_bed')

class BedUpdateView(UpdateView):
    model = Beds
    fields = ('bed_name', 'avilable_total', 'status', 'room_num',)
    template_name = 'bed_template/edit_bed_template.html'
    success_url = reverse_lazy('manage_bed')

class BedDeleteView(DeleteView):
    model = Beds
    #template_name = 'bed_template/delete_bed_template.html'
    success_url = reverse_lazy('manage_bed')
"""