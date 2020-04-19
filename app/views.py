from django.shortcuts import render
from django.http import HttpResponse
from .models import Personaldetails
from .forms import PersonaldetailsForm
# Create your views here.

def function(request):
    return render(request,'demo.html')
# def sucess(request):
#     return render(request,'app/result.html')


def getdetails(request):
    if(request.method=='POST'):
        # detail=PersonaldetailsForm(request.POST)
        # if(detail.is_valid()):
        na = request.POST.get("name")
        re=request.POST.get("register_no")
        ye=request.POST.get("year")
        per=request.POST.get("cgpa")
        ph_no=request.POST.get("ph_no")
        detail=Personaldetails(register_no=na+"_"+re,year=ye,cgpa=per,ph_no=ph_no)
        detail.save()
        return render(request,'app/result.html')
        # else:
        #     return HttpResponse("NONE")
    else:
        return HttpResponse("NONE")