from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Görünümlerinizi burada oluşturun.
def homeds(requeast):
    return HttpResponse("Hello DS")
