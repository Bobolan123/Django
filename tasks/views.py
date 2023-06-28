from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="newtask")
    priority = forms.IntegerField(label="priority", max_value=20, min_value=1)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    if request.method == "POST" and "delete" in request.POST:
        request.session["tasks"] = []
        return HttpResponseRedirect(reverse("tasks:index"))
    return render(request, "tasks/index.html", {
        "form" : request.session["tasks"]
    })
     
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST) 
        priority = NewTaskForm(request.POST)
        if form.is_valid() and priority.is_valid():
            task = form.cleaned_data["task"] # square bracket
            priority = form.cleaned_data["priority"]
            new_task = {"task": task, "priority": priority}
            request.session["tasks"].append(new_task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form" : form
            })
    
    return render(request, "tasks/add.html", {
        "form" : NewTaskForm()
    })

