from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def balaji(request):
    return HttpResponse('hi')

def cricket(request):
    return HttpResponse('<h1><marquee>Virat Kohli</h1></marquee>')

def virat(request):
    return HttpResponse('<h1><marquee>I like to Play Cricket</h1></marquee>')

def python(request):
    return HttpResponse('<h1><marquee>python is easy if you study properly</h1></marquee>')