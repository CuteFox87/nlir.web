from django.http import HttpResponse
from .models import Post
from django.shortcuts import render
 
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list' : latest_post_list}
    return render(request, 'posts/index.html', context)
