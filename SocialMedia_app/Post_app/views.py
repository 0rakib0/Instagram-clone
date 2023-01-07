from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Auth_app.models import CustomUser, Follow
from Post_app.models import Post

@login_required
def Home(request):
    follow_list = Follow.objects.filter(Follower=request.user)
    posts = Post.objects.filter(author__in=follow_list.values_list('Following'))    
    if request.method == 'GET':
        search = request.GET.get('search','')
        result1 = CustomUser.objects.filter(username=search)
        result2 = CustomUser.objects.filter(first_name__icontains=search)
    context = {
        'title':'Home | post | page',
        'search':search,
        'result1':result1,
        'result2':result2,
        'posts' : posts
    }

    return render(request, 'Post_app/home.html', context)