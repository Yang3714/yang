from django.shortcuts import render,HttpResponse

# Create your views here.
from app01 import models


def login(request):
    if request.is_ajax():
        username=request.POST.get("username")
        password=request.POST.get("password")
        ret=models.Userinfo.objects.filter(username=username,password=password)
        if ret:
            re
    return render(request,"login.html")