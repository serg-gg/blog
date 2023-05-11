from django.shortcuts import render
from django.views.generic.base import View
from .models import Post


class PostView(View):
    def get(self, request):
        posts = Post.objects.order_by('-date')
        return render(request, 'home.html', {'post_list': posts})


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog_detail.html', {'post': post})
