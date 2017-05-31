from django import template
from ..models import Post,Category

register = template.Library()

@register.simple_tag
def get_recent_posts(nums=5):
    return Post.objects.all().order_by('-created_time')[:nums]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()