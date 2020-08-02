from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of 'arg' from the string

    """
    return value.replace(arg,'')

#register.filter('cut',cut) #'cut' is the name i'm calling d filter
                        # the other cut is the name of the function
                        # that implements it.
