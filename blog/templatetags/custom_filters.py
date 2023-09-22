from django import template

register = template.Library()

@register.filter
def divide_by(value, arg):
    try:
        return int(value) // int(arg)
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def replace_h1(value):
    return value.replace(
        '<strong>', '<span class="normal-text">'
        ).replace(
        '</strong>', '</span>'
        ).replace(
        '<p>', '<span class="normal-text">'
        ).replace(
        '</p>', '</span>'
        )



