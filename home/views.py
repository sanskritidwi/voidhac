
# Django
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

def index(request):
    return render(request, 'home/index.html')



def new_index(request):
    return render(request, 'home/dashboard.html')


