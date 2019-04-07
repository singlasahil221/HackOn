from django import template


register = template.Library()


@register.filter
def duration(td):
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = (total_seconds%3600)%60
    return '{}:{}:{}'.format(hours, minutes, seconds)