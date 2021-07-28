from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'index/index.html', context=context)
