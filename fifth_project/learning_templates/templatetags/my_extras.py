from django import template

# register = template.library()
{% load my_templates %}

@register.filter(name='cut') #  a much cleaner way to do it than the currently commented out bits

def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

# register.filter('cut', cut)
