from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.htm')

def login(request):
    return render(request,'login.htm')

def reg(request):
    return render(request,'reg.htm')