from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def logoPage(request):
    return HttpResponse("<h1> Hello this is title </h1> <h2> Bye Bye Title </h2>")
