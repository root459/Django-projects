from django.shortcuts import render,HttpResponse

def index(request):
    context={
        'variable':"this is sent"#sending a dictionary with variables and values so they can be accessed by the render
    }
    return render(request,'index.html',context)


def aboutus(request):
    return render(request,'aboutus.html')
    


def contactus(request):
    return render(request,'contactus.html')
    

