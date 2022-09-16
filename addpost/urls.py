from . import views
from django.urls import path, include



app_name ="addpost"

urlpatterns=[
	path("addpost/",views.upload_room, name="upload"),
	path("room/",views.room_list, name="room"),
	path("room/<int:pk>",views.delete_room, name="delete_room"),
	path("update/<int:pk>",views.update_room,name="update_room"),

	
]