from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def is_active(context, target_path):
    if target_path == '/':
        return 'active' if target_path == context['request'].path else ''

    return 'active' if target_path in context['request'].path else ''