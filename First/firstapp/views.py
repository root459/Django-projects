from django.shortcuts import render,HttpResponse

def index(request):
    context={
        'variable':"this is sent"#sending a dictionary with variables and values so they can be accessed by the render
    }
    return render(request,'index.html',context)

def settings(request):
    return HttpResponse("this is settings")

def aboutus(request):
    return HttpResponse("this is about page")


def contactus(request):
    return HttpResponse("this is contact us page")

