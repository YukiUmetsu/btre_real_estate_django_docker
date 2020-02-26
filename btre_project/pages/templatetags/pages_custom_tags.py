from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def is_active(context, target_path):
    return 'active' if context['request'].path == target_path else ''