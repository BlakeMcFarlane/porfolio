from django.shortcuts import render
from .models import Tag, Project
from django.core.mail import send_mail
from .forms import Contact



def home(request):
    projects=Project.objects.all()
    form=Contact()
    context={
        'projects':projects
    }
    return render(request, 'home.html', context)

