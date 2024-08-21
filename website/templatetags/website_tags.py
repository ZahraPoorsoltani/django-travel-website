from django import template
from django.utils import timezone
from blog.models import Post

register = template.Library()

@register.inclusion_tag('latest-blog-posts.html')
def latest_blog_posts():
    posts = Post.objects.filter(status=1,published_date__lte= timezone.now()
                                      ).order_by('-published_date')[:6]
    return {'posts':posts}
