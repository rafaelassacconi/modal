from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from bootstrap3.models import Post
from bootstrap3.forms import PostForm


def home(request):
    context = {}
    context['posts'] = Post.objects.all()
    return render(request, 'home.html', context)


def post(request, post_id=None):
    post = None
    if post_id:
        post = get_object_or_404(Post, pk=post_id)

    form = PostForm(request.POST or None, instance=post)

    if request.POST:
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, u'Post saved.')
        else:
            messages.add_message(request, messages.ERROR, u'Check the informations bellow.')

    context = {}
    context['form'] = form
    return render(request, 'post.html', context)
