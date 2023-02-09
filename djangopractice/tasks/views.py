from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
#tasks = ["foo","bar","baz"]
# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task") #inputs for the form
    priority = forms.IntegerField(label="Priority", min_value=1,max_value=10)

def index(request):
    if "tasks" not in request.session: #make the 'task' variable session based
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST": #if the user submitted some form data
        form = NewTaskForm(request.POST) #param has all the data the user submitted when the user pressed submit
        if form.is_valid():
            task = form.cleaned_data["task"] #variable containing all the cleaned data defined in the NewTaskForm class
            request.session["tasks"] += [task] #change the tasks variable's data
            return HttpResponseRedirect(reverse("tasks:index")) #reverse means figure out what thee url of the tasks index url is
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
        
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })