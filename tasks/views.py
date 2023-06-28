from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="newtask")
    priority = forms.IntegerField(label="priority", max_value=10, min_value=1)

def index(request):     
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks" : request.session["tasks"]
    })
     
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST) 
        if form.is_valid():
            task = form.cleaned_data["task"] # square bracket
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form" : form
            })
    
    return render(request, "tasks/add.html", {
        "form" : NewTaskForm()
    })

