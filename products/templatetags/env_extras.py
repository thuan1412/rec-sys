import os
from django import template

register = template.Library()


@register.simple_tag
def env_extras(key):
    # print("get env key", key, os.environ.get(key))
    return os.environ.get(key)
