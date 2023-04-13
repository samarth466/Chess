from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse
from django.views.decorators.http import require_safe, require_http_methods
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from blogs.models import Post, Comment
from blogs.forms import PostForm, CommentForm
from authentication.models import User

# Create your views here.


@require_safe
def home(request):
    posts = Post.objects.all()
    return render(request, "blogs/home.html", {'posts': posts})


@require_safe
def details(request, title: str):
    post = get_object_or_404(Post, title=title)
    return render(request, "blogs/details.html", {'post': post})


@login_required
@require_http_methods(["GET", "POST"])
def create_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "blogs/create_post.html", {'form': form})
    elif request.method == "POST":
        user = request.user
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            publication_date = form.cleaned_data["publication_date"]
            p = Post(title=title, content=content,
                     publication_date=publication_date)
            p.save()
            return HttpResponse("Successfully created post.", status=201)


@require_http_methods(["GET", "POST"])
@login_required
def add_comment(request, title: str):
    if request.method == "GET":
        form = CommentForm()
        return render(request, "blogs/add_comment.html", {'form': form})
    elif request.method == "POST":
        user = request.user
        post = get_object_or_404(Post, title=title)
        post.comment_count += 1
        post.save(update_fields=["comment_count"])
        if form.is_valid():
            content = form.cleaned_data["content"]
            comment = Comment(post=post, content=content)
            comment.save()
            return HttpResponse("Successfully created comment.", status=201)


@api_view(["DELETE"])
def delete_post(request, title: str):
    user = request.user
    staff_condition = user.is_superuser or user.is_admin or (
        user.is_staff and user.has_perm('blogs.delete_post'))
    post = get_object_or_404(Post, title=title)
    if user != post.author and not staff_condition:
        return Response({"data": "You must be the author to delete a post."}, status=status.HTTP_403_FORBIDDEN)
    for comment in post.comments:
        comment.delete()
    post.delete()
    return Response({"data": "Post successfully deleted."}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_comment(request, id: int):
    user = request.user
    comment = get_object_or_404(Comment, id=id)
    staff_condition = user.is_superuser or user.is_staff or (
        user.is_staff and user.has_perm('blogs.delete_comment'))
    if user != comment.author and not staff_condition:
        return Response({"data": "You must be the author to delete a comment."}, status=status.HTTP_403_FORBIDDEN)
    comment.delete()
    return Response({"data": "Comment successfully deleted."}, status=status.HTTP_200_OK)
