from django.core.exceptions import ValidationError

def validate_number(value):
    any = str(value)
    if len(str(value)) != 10:
        raise ValidationError(
            "Please enter valid contact number"
        )
    elif any.isnumeric() == True:
        ValidationError(
            "Please enter valid number"
        )
