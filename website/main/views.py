from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h4>Hello</h4>')


def page_1(request):
    return HttpResponse('<h1>This is page_1</h1>')
