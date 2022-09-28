from base64 import b64encode
from django import template



register = template.Library()



@register.filter
def binary_image(_bin):
    if _bin is not None: return b64encode(_bin).decode('utf-8')