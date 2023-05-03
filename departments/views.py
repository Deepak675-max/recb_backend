from django.shortcuts import render, redirect
from .models import department
from .forms import MyForm


class User:
    def __init__(self, name, summary, image, total_students):
        self.name = name
        self.summary = summary
        self.image = image
        self.total_students = total_students


def create_department(request):
    if request.method == "POST":
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = User(form.cleaned_data['title'], form.cleaned_data['summary'],
                        form.cleaned_data['image'], form.cleaned_data['total_students'])
            return render(request, 'home.html', {'department': user})
    else:
        form = MyForm()
        return render(request, 'department/department.html', {'form': form})
