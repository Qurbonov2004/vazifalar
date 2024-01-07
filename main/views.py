from django.shortcuts import render 
from django.http import HttpResponse
from .models import Service,Mashgulot,Teacher,Contact_Us


def main(request):
    return render(request,'index.html')




