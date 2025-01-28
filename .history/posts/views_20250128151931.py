from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Index View
from django.core.paginator import Paginator

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)  # Sayfa başına 5 post
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/index.html', {'page_obj': page_obj})


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
    print(f"Post ID: {post.pk}")  # Debugging statement

    if post.author != request.user:
        return redirect('index')  # Unauthorized access

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'posts/post_update.html', {'form': form, 'post': post})



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