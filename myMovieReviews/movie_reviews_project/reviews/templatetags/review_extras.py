
from django import template

register = template.Library()

@register.filter
def format_runtime(minutes):
    """정수 형태의 '분'을 '시간 분' 형태의 문자열로 변환합니다."""
    if minutes is None or not isinstance(minutes, int):
        return ""

    hours = minutes // 60
    mins = minutes % 60

    if hours > 0:
        return f"{hours}시간 {mins}분"
    else:
        return f"{mins}분"