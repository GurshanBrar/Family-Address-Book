from django import template
import math

register = template.Library()
@register.filter(name='forloop')
def forloop(number):
    return range(math.ceil(int(number)/3))

@register.filter(name='num')
def num(number):
    return math.ceil(int(number)/3)
