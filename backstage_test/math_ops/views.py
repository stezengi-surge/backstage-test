from http import HTTPStatus

from django.views import View
from django.http import JsonResponse

from .forms import DifferenceForm
from .models import difference_math_logic

class DifferenceView(View):
    def get(self, request, *args, **kwargs) -> JsonResponse:
        difference_form = DifferenceForm(request.GET)
        if difference_form.is_valid():
            number = difference_form.cleaned_data.get('number')
            response = difference_math_logic.get_difference_response(number=number)
            return JsonResponse(response)
        else:
            return JsonResponse(
                {
                    'success': False, 
                    'errors': dict(difference_form.errors.items())
                },
                status=HTTPStatus.UNPROCESSABLE_ENTITY
            )
    