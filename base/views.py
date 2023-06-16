from django.shortcuts import render
from .models import Tag, Project
from django.core.mail import send_mail
from .forms import Contact
from django.conf import settings



def home(request):
    form=Contact()
    context={
        'form':form,
    }
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        contact_form = str(name + ' \n - ' + email + ' \n  - ' + subject)
        print (contact_form)
        send_mail('Contact Form',
                    contact_form, 
                    settings.EMAIL_HOST_USER,
                    ['theblakemcfarlane@gmail.com'],
                    fail_silently=False)
                  
    return render(request, 'home.html', context)

