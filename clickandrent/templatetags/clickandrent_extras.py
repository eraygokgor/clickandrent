from django import template
from base64 import b64encode

register = template.Library()

@register.filter("mongo_id")
def mongo_id(value):
    return str(value['_id'])
