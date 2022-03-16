from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import *

# Create your views here.
def add_post(request):
    context = {}
    if request.user.is_staff:
        if request.method == 'POST':
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                return HttpResponseRedirect(request.path_info)

            blog_form = BlogPostForm(request.POST,request.FILES)

            if blog_form.is_valid():
                blog_object = blog_form.save(commit=False)
                blog_object.author = request.user
                blog_object.save()
                print(blog_object.pk)
                return view_post(request,blog_object.pk)
        else:
            blog_form = BlogPostForm()
            category_form = CategoryForm()
        context['blog_form'] = blog_form
        context['category_form'] = category_form
        return render(request,'add_post.html',context)
    else:
        context['message'] = "Sorry! You are not allowed to access this page"
        return render(request,'not_allowed.html',context)

def view_post(request,pk=1):
    context = {}
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = Post.objects.get(pk=pk)
                comment.save()
            return HttpResponseRedirect(request.path_info)
        else:
            context['message'] = "Sorry! You are not allowed to post into this url"
            return render(request,'not_allowed.html',context)

    else:
        blog_post = Post.objects.get(pk=pk)
        if blog_post != None:
            context['post'] = blog_post
            comment_form = CommentForm()
            context['comment_form'] = comment_form
            context['categories'] = Category.objects.all()
            return render(request,'view_post.html',context)
        else:
            return add_post(request)
def view_category_post(request,name):
    context = {}
    posts = Category.objects.get(name=name).post_set.all()
    category = Category.objects.get(name=name)
    context['category'] = category
    context['posts'] = posts
    print(posts)
    return render(request,'view_post_categories.html',context)    
    