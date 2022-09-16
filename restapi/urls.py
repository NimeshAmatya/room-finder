from django.urls import path
from addpost import views
from start import views
from restapi import views

app_name = "restapi"

urlpatterns = [
    path("getallapi/", views.show_all_data, name="show_all_data"),
    path('getapi/<int:pk>/', views.get_data, name="get_data"),
    path('updateapi/<int:pk>/', views.update_data, name="update_datan"),
    path('deleteapi/<int:pk>/', views.delete_data, name="delete_data"),
    path('postapi', views.post_data, name="post_data"),
    path('page/<int:PAGENO>/<int:SIZE>/', views.movie_objects_pagination, name="movie_objects_pagination")
]