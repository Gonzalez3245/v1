from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm



def index(request):
    posts = BlogPost.objects.all()
    context = {'posts':posts}
    return render(request, 'home.html', context)

def post_view(request, pk):
    posts = BlogPost.objects.get(id=pk)

    return render(request, 'post_view.html', {'post':posts})

def create_post(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'create_post.html', context)

def update_post(request, pk):
    post = BlogPost.objects.get(id=pk)
    form = BlogPostForm(instance=post)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'create_post.html', {'post':post, 'form':form})


def deletepost(request, pk):
    post = BlogPost.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'delete_post.html', {'post':post})