from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author
from .forms import PostForm
from django.urls import reverse

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def index(request):
    queryset = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': queryset,
    }
    return render(request, 'index.html', context)

def blog(request):
    queryset = Post.objects.order_by('-timestamp')

    context = {
        'blog_list': queryset,
    }
    return render(request, 'blog.html', context)


def blogdetail(request, id):
    blog = get_object_or_404(Post, id=id)
    context = {
        'blog': blog,
    }
    return render(request, 'single-blog.html', context)

'''
def about(request, id):
    author = get_object_or_404(Author, id=id)
    blog = get_object_or_404(Post, id=id)
    context = {
        'person': author,
        'blog': blog,
    }
    return render(request, 'about.html', context)
'''
def blog_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("blog-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "blog_create.html", context)

def blog_update(request, id):
    title = 'Update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(
        request.POST or None, 
        request.FILES or None, 
        instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("blog-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "blog_create.html", context)

def blog_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("blog-list"))


def contact(request):
    return render(request, 'contact.html', {})