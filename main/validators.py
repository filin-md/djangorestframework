import re

from rest_framework.serializers import ValidationError

BLOCKED_LINKS = ['youtube.com']

def validator_links(value):
    if 'youtube.com' not in value.lower():
        raise ValidationError('Можно указывать ссылки только на youtube.com')
