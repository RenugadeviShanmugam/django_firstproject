from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     msg='<h1>Welcome to Django Framework</h1>'
#     return HttpResponse(msg)

# def user(request):
#     return HttpResponse('<h1>This is User page</h1>')

# def home(request):
#     return render(request,'home.html')

# def product(request):
#     monitor_price=int(request.GET["monitor"])
#     keyboard_price=int(request.GET["keyboard"])
#     printer_price=int(request.GET["printer"])
#     result=monitor_price+keyboard_price+printer_price
#     return render(request,'result.html',{'Result':result})

def index(request):
    return render(request,'index.html')

def register(request):
    reg_name=request.POST["name"]
    reg_pass=request.POST["password"]
    reg_addr=request.POST["address"]
    reg_email=request.POST["email"]
    return render(request,'output.html',{'Name':reg_name,'Password':reg_pass,'Address':reg_addr,'Email':reg_email})

def homeimage(request):
    return render(request,'homeimage.html')

def homebootstrap(request):
    return render(request,'homebootstrap.html')

def test(request):
    return render(request,'test.html')