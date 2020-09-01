from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    blog = Blog.objects
    return render(request,'blog/home.html',{'blog':blog})

def details(request,blog_id):
    blog = get_object_or_404(Blog,pk = blog_id)
    return render(request, 'blog/details.html',{'blog':blog})
    
