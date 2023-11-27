from django.shortcuts import render,HttpResponse
from firstapp.models import Contact
from datetime import datetime
from django.contrib import messages
def index(request):
    context={
        'variable':"this is sent"#sending a dictionary with variables and values so they can be accessed by the render
    }
    messages.success(request,"this is a text message")
    return render(request,'index.html',context)


def aboutus(request):
    return render(request,'aboutus.html')
    


def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "your message has been sent")


    return render(request,'contactus.html')

