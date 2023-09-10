import datetime
from django.test import TestCase
from .models import DifferenceStatsModel, difference_math_logic

class DifferenceStatsModelCase(TestCase):
    def setUp(self):
        DifferenceStatsModel.objects.create()

    def test_save(self):
        difference_stats_object = DifferenceStatsModel.objects.filter().first()
        self.assertEqual(difference_stats_object.occurrences, 1)
        self.assertEqual(
            difference_stats_object.last_datetime.isoformat(sep=" ", timespec="seconds"), 
            datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
        )
    
    def test_log_new_occurance(self):
        DifferenceStatsModel.objects.log_new_occurance()
        difference_stats_object = DifferenceStatsModel.objects.filter().first()
        self.assertEqual(difference_stats_object.occurrences, 2)
        self.assertEqual(
            difference_stats_object.last_datetime.isoformat(sep=" ", timespec="seconds"), 
            datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
        )
    
    def test_get_difference_stat(self):
        difference_stats_object = DifferenceStatsModel.objects.get_difference_stat()
        self.assertEqual(difference_stats_object.occurrences, 1)
        self.assertEqual(
            difference_stats_object.last_datetime.isoformat(sep=" ", timespec="seconds"), 
            datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
        )


class DifferenceMathLogicCase(TestCase):

    def test_sum_of_squares(self):
        sum_of_squares = difference_math_logic.sum_of_squares(number=10)
        self.assertEqual(sum_of_squares, 385)
    
    def test_square_of_sum(self):
        sum_of_squares = difference_math_logic.square_of_sum(number=10)
        self.assertEqual(sum_of_squares, 3025)
    
    def test_square_of_sum(self):
        occurances_and_last_datetime = difference_math_logic.get_occurances_and_last_datetime()
        self.assertEqual(occurances_and_last_datetime["occurrences"], 1)
        self.assertEqual(
            occurances_and_last_datetime["last_datetime"], 
            None
        )
    
    def test_get_difference_value(self):
        difference_value = difference_math_logic.get_difference_value(number=10)
        self.assertEqual(difference_value, 2640)

    def test_square_of_sum_on_2nd_occurance(self):
        DifferenceStatsModel.objects.log_new_occurance()
        occurances_and_last_datetime = difference_math_logic.get_occurances_and_last_datetime()
        self.assertEqual(occurances_and_last_datetime["occurrences"], 2)
        self.assertEqual(
            occurances_and_last_datetime["last_datetime"].isoformat(sep=" ", timespec="seconds"), 
            datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
        )

    def test_get_difference_response(self):
        difference_response = difference_math_logic.get_difference_response(number=10)
        self.assertEqual(difference_response["occurrences"], 1)
        self.assertEqual(difference_response["last_datetime"], None)
        self.assertEqual(difference_response["value"], 2640)
        self.assertEqual(
            difference_response["datetime"].isoformat(sep=" ", timespec="seconds"), 
            datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
        )
        self.assertEqual(difference_response["number"], 10)
    
