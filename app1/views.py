from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bala(request):
    return HttpResponse('<h1>i love u akhila</h1>')

def balu(request):
    return HttpResponse('<h1><marquee>ravi teja fan</marquee></h1>')