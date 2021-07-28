from django.shortcuts import render

def problem(request):
    context = {}
    context['order_list'] = range(185)
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'resource/problem.html', context=context)
