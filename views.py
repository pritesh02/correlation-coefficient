from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Pritesh'})

def add(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    val3 = int(request.GET["num3"])
    val4 = int(request.GET["num4"])
    val5 = int(request.GET["num5"])
    val6 = int(request.GET["num6"])
    val7 = int(request.GET["num7"])
    val8 = int(request.GET["num8"])  
    valy1 = int(request.GET["numy1"])
    valy2 = int(request.GET["numy2"])
    valy3 = int(request.GET["numy3"])
    valy4 = int(request.GET["numy4"])
    valy5 = int(request.GET["numy5"])
    valy6 = int(request.GET["numy6"])
    valy7 = int(request.GET["numy7"])
    valy8 = int(request.GET["numy8"])
    meanofx = (val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8)/8
    meanofy =(valy1 + valy2 + valy3 + valy4 + valy5 + valy6 + valy7 + valy8)/8


    return render(request, "result.html",{'result':meanofx})