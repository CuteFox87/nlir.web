from django.shortcuts import render, get_object_or_404
from .models import Problem
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone
from django.urls import reverse

def problem(request):
    context = {}
    if request.user.is_authenticated:
        context['order_list'] = request.user.problem_set.order_by('-problem_order')
        context['is_authenticated'] = True

    return render(request, 'resource/problem.html', context=context)

def updateResult(request):
    if request.POST['result'] and request.POST['problem_order']:
        if request.POST['result'] == 'x':
            p = get_object_or_404(Problem, problem_order = int(request.POST['problem_order']))
            p.delete()
        else:
            p = Problem(user = request.user, problem_order = int(request.POST['problem_order']), result = request.POST['result'], date = timezone.now())
            p.save()
        return HttpResponseRedirect(reverse('resource:problem'))
    else:
        raise Http404("invalid query parameters")
