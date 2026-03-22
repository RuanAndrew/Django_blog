from django.shortcuts import render, get_object_or_404
from .models import Post

def list(request):
    posts = Post.objects.all()

    return render(request, 'posts/list.html', {'posts': posts})
def details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'posts/details.html', {'post': post})

