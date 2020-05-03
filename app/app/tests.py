from django.test import TestCase
from app.calc import sum 

class CalcTests(TestCase):
    def test_1_sum(self):
        "Check That sum should be Same"
        self.assertEqual(sum(4,5), 9)


    def test_3_valid_sum(self):
        "We enter values and check results not same"
        self.assertEqual(sum(3,4), 7)
