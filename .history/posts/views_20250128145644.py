from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Index View
def index(request):
    posts = Post.objects.all().order_by('-created_at')  # Gönderileri tarihe göre sırala
    return render(request, 'posts/index.html', {'posts': posts})

# Post Detail View
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

# Create Post View
@login_required
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

# Update Post View
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('index')  # Unauthorized access

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            print(f"Form successfully saved for post: {post.pk}")
            return redirect('post_detail', pk=post.pk)
        else:
            print("Form errors:", form.errors)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_update.html', {'form': form})


# Delete Post View
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('index')  # Yetkisiz erişimi engelle
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'posts/post_delete.html', {'post': post})