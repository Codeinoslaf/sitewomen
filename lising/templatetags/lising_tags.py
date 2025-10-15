from django import template
from lising.models import Category, TagPost

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('leasing_equipment/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Category.objects.all()
    return {"cats": cats, "cat_selected": cat_selected_id}


@register.inclusion_tag('leasing_equipment/list_tags.html')
def show_all_tags():
    return {"tags": TagPost.objects.all()}

