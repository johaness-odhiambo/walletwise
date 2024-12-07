from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Enquiries

# Create your views here.
def home_page(request):
    return render(request, 'index.html')
def contact_page(request):
    # funtion to push enquiries to db
    
    if request.method == 'POST':
        # variables to pic the input
        enquiries = Enquiries(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']
        )
        # save the variables
        enquiries.save()
        return redirect( 'expenses:home')
    else:
        enquiries = Enquiries.objects.all()
        context ={
        'enquiries': enquiries
    }

        return render(request, 'contact.html', context)
