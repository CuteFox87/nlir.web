from django.shortcuts import render
from .models import Project

def display(request):
    context = {
        'project_list' : Project.objects.order_by('-pk')
    }
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'display/display.html', context=context)
