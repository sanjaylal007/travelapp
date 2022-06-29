from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def function(request):
    passingvalue="darknet"
    return render(request,"darknet.html",{'obj':passingvalue})
def function2(request):
    return render(request,"home.html")
def function3(request):
    return HttpResponse("iam the one")
def addition(request):
    x=int(request.GET["num1"])
    y=int(request.GET["num2"])
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y

    return render(request,"result.html",{'obj':add,'object1':sub,'object2':mul,'object':div})
