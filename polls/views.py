from django.shortcuts import render

# Create your views here.
# filepath: c:\Users\Asus ROG\Downloads\.vscode\mydjangoapp\mysite\polls\views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
