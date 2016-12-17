# coding=utf-8
from __future__ import unicode_literals, print_function

from datetime import date

from django import template

register = template.Library()


@register.filter(name='format_timestamp')
def format_timestamp(timestamp):
    return date.fromtimestamp(timestamp).strftime('%Y-%m-%d')


@register.filter(name='query_dict_string')
def query_dict_string(query_dict):
    try:
        return ' '.join([i[1] for i in query_dict.values_list()])
    except AttributeError:
        return ''
