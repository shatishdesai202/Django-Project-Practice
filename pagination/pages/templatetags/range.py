from django import template

register = template.Library()


@register.filter(name='range')
def filter_range(start, end):
  return range(start, end)

@register.filter(name="minusvalue")
def minusvalue(val):
  return val-1

@register.filter(name="plusvalue")
def plusvalue(val):
  return val+1