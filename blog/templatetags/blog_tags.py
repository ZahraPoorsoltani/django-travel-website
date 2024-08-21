from django import template
from blog.models import Post,Category
from django.utils import timezone
from django.contrib.auth.models import User
register = template.Library()


@register.inclusion_tag('blog-latest-post.html')
def latest_post():
    posts = Post.objects.filter(status=1,published_date__lte= timezone.now()
                                      ).order_by('-published_date')[:5]
    return {'posts':posts}

@register.inclusion_tag('blog-post-categories.html')
def post_categories():
    posts = Post.objects.filter(status=1,published_date__lte= timezone.now())
    cats = Category.objects.all()
    cat_dict = {}
    for cat in cats:
        cnt_post = posts.filter(category=cat).count()
        cat_dict[cat.name]=cnt_post
    return {'cats_posts':cat_dict}    

