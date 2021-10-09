from django import template
from vins.models import Category, Tag


register = template.Library()


@register.inclusion_tag('mytag-list.html')
def get_tag_list():
    return {'tags': Tag.objects.all(), 'counter': Tag.objects.filter().count()}


@register.inclusion_tag('mycategory-list.html')
def get_category_list():
    return {'cats': Category.objects.all(), 'counter': Category.objects.filter().count()}