from django.shortcuts import render

def display(request):
    context = {}
    context['list'] = range(10)
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'display/display.html', context=context)
