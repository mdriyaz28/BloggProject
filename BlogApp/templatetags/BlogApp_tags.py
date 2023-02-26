from  django import template
from BlogApp.models import Post
register=template.Library()

@register.simple_tag
def total_post():
    return Post.objects.count()

@register.inclusion_tag('BlogApp/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts=Post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

from django.db.models import Count
#@register.assignment_tag 	#not-working
@register.simple_tag		#hence use simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]