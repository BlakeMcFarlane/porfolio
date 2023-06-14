from django.shortcuts import render
from .models import Tag, Project


def home(request):
    projects=Project.objects.all()
    context={
        'projects':projects
    }
    return render(request, 'home.html', context)

