from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("this is homepage")

def settings(request):
    return HttpResponse("this is settings")

def about(request):
    return HttpResponse("this is about page")


def services(request):
    return HttpResponse("this is service page")
