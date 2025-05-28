
from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x = 20
    y = 300
    return y

def disc(request):
    x = calculate()
    return render(request,'main.html',{'name':'guru','cal':x})


    
    


