from django.shortcuts import render
from . models import Place,Name
def demo1(request):
    obj=Place.objects.all()
    run=Name.objects.all()
    return  render(request,"index.html",{'result':obj,'do':run})

def home(request):
    return  render(request,"home.html")

def about(request):
    return  render(request,"about.html")

def contact(request):
    return  render(request,"contact.html")

def thanks(request):
    lo="INDIA"
    return  render(request,"thanks.html", {'post':lo})



