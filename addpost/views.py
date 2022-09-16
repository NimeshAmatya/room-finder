from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import AddForm
from .models import Room
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json


from django.db.models import Q
# Create your views here.

#uploads room using addform and redirect to roomlist
def upload_room(request):
	form = AddForm()
	if request.method == "POST":
		form = AddForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('addpost:room')
	return render(request,"addpost/upload.html", {"form":form})		

#Stores the uploaded rooms in list
def room_list(request):
	room = Room.objects.all()

	query = ""
	if request.GET:
		query = request.GET['q']

		room = get_data_queryset(str(query))

	return render(request,"addpost/room_list.html",{"rooms":room})	

#Deletes specific room having the related id/pk
def delete_room(request, pk):

	room = Room.objects.get(pk=pk)
	room.delete()
	return redirect('addpost:room')

#Updates specific room having the related id/pk
def update_room(request,pk):

	room = get_object_or_404(Room,pk=pk)
	print(room)
	if request.method == "POST":
		location = request.POST['location']
		description = request.POST['description']
		price = request.POST['price']
		room.location = location
		room.description = description
		room.price = price
		room.save()
		return redirect('addpost:room')

	return render(request,"addpost/update.html",{"room":room})

#Search the room with the location
def get_data_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		rooms = Room.objects.filter(
			Q(location__icontains=q)
			).distinct()

		for room in rooms:
			queryset.append(room)
	return list(set(queryset))		
