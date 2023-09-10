from django.db import models
import datetime
from typing import TypedDict


class DifferenceStatsManager(models.Manager):

    def log_new_occurance(self) -> None:
        difference_stat = super().get_queryset().first()
        if difference_stat:
            difference_stat.save()
        else:
            difference_stat = DifferenceStatsModel()
            difference_stat.save()
    
    def get_difference_stat(self):
        difference_stat = super().get_queryset().first()
        return difference_stat


class DifferenceStatsModel(models.Model):
    occurrences = models.IntegerField(default=0)
    last_datetime = models.DateTimeField(blank=True)

    objects = DifferenceStatsManager()

    def save(self, *args, **kwargs):
        self.occurrences += 1
        self.last_datetime = datetime.datetime.now()
        super().save(*args, **kwargs)


class DifferenceResponse(TypedDict):
    occurrences: int
    last_datetime: datetime.datetime
    datetime: datetime.datetime
    sum_of_squares: int
    square_of_sum: int
    number: int


class DifferenceMathLogic(object):
    def sum_of_squares(self, number: int) -> int:
        return sum([i ** 2 for i in range(1, number+1)])

    def square_of_sum(self, number: int) -> int:
        return sum([i for i in range(1, number+1)]) ** 2
    
    def get_difference_value(self, number: int) -> int:
        sum_of_squares = self.sum_of_squares(number=number)
        square_of_sum = self.square_of_sum(number=number)
        return abs(square_of_sum - sum_of_squares)

    def get_occurances_and_last_datetime(self) -> DifferenceResponse: 
        difference_stat = DifferenceStatsModel.objects.get_difference_stat()

        occurances_and_last_datetime = {}
        if difference_stat: 
            occurances_and_last_datetime['occurrences'] = difference_stat.occurrences + 1
            occurances_and_last_datetime['last_datetime'] = difference_stat.last_datetime
        else:
            occurances_and_last_datetime['occurrences'] = 1
            occurances_and_last_datetime['last_datetime'] = None
        
        return occurances_and_last_datetime
    
    def get_difference_response(self, number: int) -> DifferenceResponse:
        response_data = self.get_occurances_and_last_datetime()
        response_data['value'] = self.get_difference_value(number=number)
        response_data['datetime'] = datetime.datetime.now()
        response_data['number'] = number

        DifferenceStatsModel.objects.log_new_occurance()

        return response_data


difference_math_logic = DifferenceMathLogic()