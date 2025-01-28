from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})