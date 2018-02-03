# creating own custom filter
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out all value of "arg" from the string
    """
    return value.replace(args,'')

# register.filter('cut',cut)
