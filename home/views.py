from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context ={
        "variable1":"sp is great",
        "variable2":"you are great"
    }
   # messages.success(request,"this is test message")
    return render(request, "index.html",context)
    #return HttpResponse(" this is home page")

def about(request):
        return render(request, "about.html")

    #return HttpResponse(" this is about page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        number = request.POST.get('Number')
        description = request.POST.get('Description')
        
        print("Name:", name)
        print("Email:", email)
        print("Number:", number)
        print("Description:", description)
        
        instance = Contact(Name=name, Email=email, Number=number, Description=description)
        instance.save()
        messages.success(request,'your message has been sent')
        return render(request, "contact.html")
        
    return render(request, "contact.html")

    #return HttpResponse(" this is contact page")

def service(request):
        return render(request, "services.html")

    #return HttpResponse(" this is service page")