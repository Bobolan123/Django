from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="newtask")
    priority = forms.IntegerField(label="priority", max_value=20, min_value=1)

def index(request):
    tasks = request.session.get("tasks", [])  # Retrieve tasks from session or default to an empty list
    if request.method == "POST" and "delete" in request.POST:
        request.session["tasks"] = []  # Clear tasks list in session
        return redirect("tasks:index")
    return render(request, "tasks/index.html", {"tasks": tasks})

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            priority = form.cleaned_data["priority"]
            new_task = {"task": task, "priority": priority}

            tasks = request.session.get("tasks", [])  # Retrieve tasks from session or default to an empty list
            tasks.append(new_task)
            request.session["tasks"] = tasks

            return redirect("tasks:index")
    else:
        form = NewTaskForm()

    return render(request, "tasks/add.html", {"form": form})