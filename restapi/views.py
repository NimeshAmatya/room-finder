
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt

from addpost.forms import AddForm
from addpost.models import Room

# restapi get all model data
def show_all_data(request):
	room = Room.objects.all()
	print(type(room))
	dict_type = {"Room": list(room.values("location", "description", "price"))}
	return JsonResponse(dict_type)

# restapi get specific model data by id in json format
def get_data(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"Location": room.location, "Description": room.description, "Price": room.price})

# restapi updates specific data by respective id
@csrf_exempt
def update_data(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"Location": room.location, "Description": room.description, "Price": room.price})
    else:
        json_body = request.body.decode('utf-8')
        json_data = json.loads(json_body)
        room.location = json_data['location']
        room.description = json_data['description']
        room.price = json_data['price']
        
        room.save()
        return JsonResponse("Updated !", safe=False)

# The restapi deletes the data having specific pk/id
@csrf_exempt
def delete_data(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"Location": room.location, "Description": room.description, "Price": room.price})
    else:
        room.delete()
        return JsonResponse("Deleted !", safe=False)

# restapi post model data
@csrf_exempt
def post_data(request):
    if request.method == "POST":
        room = Room()
        json_body = request.body.decode('utf-8')
        json_data = json.loads(json_body)
        room.pdf = json_data['pdf']
        room.location = json_data['location']
        room.description = json_data['description']
        room.price = json_data['price']
        room.save()
        return JsonResponse("Uploaded!", safe=False)


# restapi pagination with size and pageno params
@csrf_exempt
def movie_objects_pagination(request,PAGENO,SIZE):
    skip = SIZE * (PAGENO -1)
    room = Room.objects.all() [skip:(PAGENO * SIZE)]
    dict = {
        "room": list(room.values("pdf","location","description","price"))
    }
    return JsonResponse(dict)