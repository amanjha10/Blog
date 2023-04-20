from django.shortcuts import render
from blog.models import Post
# Create your views here.

def home(request):

    post=Post.objects.all()[:11]
    print(post)
    data= {
        'posts':post,
    }
    return render(request,'home.html',data)
