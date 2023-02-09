from django.urls import path

from . import views

app_name = "tasks" #the app named is used for non hard coded links
urlpatterns = [
     path("",views.index,name="index"),
     path("add", views.add, name="add")
]