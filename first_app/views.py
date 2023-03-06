from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    '''首页'''
    return render(request, './dist/index.html')
