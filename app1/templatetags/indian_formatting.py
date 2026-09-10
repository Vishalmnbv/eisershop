from django import template
register = template.Library()
@register.filter(name='format_indian_currency')
def format_indian_currency(value):
    if value is None or value == "" or value == 0:
        return "0"
    try:
        val = int(round(float(value)))
    except (ValueError, TypeError):
        return str(value)
    if val == 0:
        return "0"
    val_str = str(val)
    if len(val_str) <= 3:
        return val_str
    last_three = val_str[-3:]
    other_digits = val_str[:-3]
    formatted_other = ""
    while len(other_digits) > 2:
        formatted_other = "," + other_digits[-2:] + formatted_other
        other_digits = other_digits[:-2]
    if other_digits:
        formatted_other = other_digits + formatted_other
    return formatted_other + "," + last_three