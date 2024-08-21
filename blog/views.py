from django.shortcuts import render,get_object_or_404
from blog.models import Post
import datetime
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def blog_view(request,**kwargs):
    posts = Post.objects.filter(published_date__lte= timezone.now(),status=1)
   

    if kwargs.get('cat_name')!=None:
        posts =posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username')!=None:
        posts = posts.filter(author__username=kwargs['author_username'])


    try:
        page_number =  request.GET.get('page')        
        paginator = Paginator(posts,3)
        page_obj = paginator.get_page(page_number)   

    except EmptyPage:
        page_obj = paginator.get_page(1) 
    except PageNotAnInteger:
        page_obj = paginator.get_page(1) 
        
        
    return render(request,'blog-home.html',{'posts':page_obj})



def blog_single(request,post_id):
    post = get_object_or_404(Post,id=post_id,status = 1,published_date__lte= timezone.now())
    post.counted_view +=1
    post.save()
    prev_post = Post.objects.filter(id__lt=post_id,status=1,published_date__lte= timezone.now()
                                 ).order_by('-id')
    
    next_post = Post.objects.filter(id__gt=post_id,status=1,published_date__lte= timezone.now()
                                 ).order_by('id')
    

    if len(prev_post):
        prev_post = prev_post[0]

    if len(next_post):
        next_post = next_post[0]

    content = {"prev_post":prev_post,"next_post":next_post,'post':post}
    return render(request,'blog-single.html',content)

def blog_search(request):
    posts = Post.objects.filter(published_date__lte= timezone.now(),status=1)
    if request.method == 'GET':
        if s:=request.GET.get('s'):
            posts =posts.filter(content__contains=s)
        
    return render(request,'blog-home.html',{'posts':posts})


def test(request,name):
    return HttpResponse(name)