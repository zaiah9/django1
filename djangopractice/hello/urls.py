from django.urls import path
from . import views #. means the current directory
urlpatterns = [
    path("<str:name>",views.greet,name="greet"),
    path("",views.index, name="index"),
    path("brian",views.brian, name="brian")
    
]

