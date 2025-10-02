from django import template
import lising.views as views

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.equipment_db


@register.inclusion_tag('leasing_equipment/list_categories.html')
def show_categories(cat_selected=0):
    cats = views.equipment_db
    return {"cats": cats, "cat_selected": cat_selected}

