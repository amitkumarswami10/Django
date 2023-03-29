from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

def index(request):
    #return HttpResponse("this is homepage")
    context = {
        'variable':"this is sent"
    }
    
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is aboutpage")
def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is servicespage")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact= Contact(name=name,email=email,desc=desc)
        contact.save()
        messages.success(request, 'Your Message has been Sent !')
    return render(request,'contact.html')
    #return HttpResponse("this is contactpage")

# Create your views here.
