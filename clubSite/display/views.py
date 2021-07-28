from django.shortcuts import render

def display(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'display/display.html', context=context)
