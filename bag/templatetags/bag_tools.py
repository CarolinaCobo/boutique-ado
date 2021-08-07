from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def cal_subtotal(prize, quantity):
    return prize * quantity
