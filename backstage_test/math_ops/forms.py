from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _ 
from django import forms


def validate_number(value: int) -> None:
    if not (value > 0 and value <= 100):
        raise ValidationError(
            _("Given number must be greater than 0 and less than or equal to 100")
        )
        
class DifferenceForm(forms.Form):
    number = forms.IntegerField(validators=[validate_number])
