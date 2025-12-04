from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import CreateBlog

# Create your views here.

def home_fun(request):
    posts = CreateBlog.objects.all().order_by('-created_at')
    return render(request,'home.html',{'posts': posts})

def result_fun(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        #validating box
        if title == "" or content == "":
            return redirect('home')

        #save to database
        CreateBlog.objects.create(
            title = title,
            content = content 
        )
    return redirect('home')

def update_fun(request,post_id):
    post = get_object_or_404(CreateBlog,id=post_id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect("home")

    return render(request, 'update.html', {'posts':post})

def delete_fun(request, post_id):
    post = get_object_or_404(CreateBlog, id=post_id)
    post.delete()
    return redirect('home')
