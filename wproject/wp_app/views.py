from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def theme(request):
    return render(request, 'theme.html', {})