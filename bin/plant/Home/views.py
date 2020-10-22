from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from . import models

def SearchView(request):

    return  HttpResponse('hi')