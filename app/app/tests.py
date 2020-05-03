from django.test import TestCase
from app.calc import adding_sum


class CalcTests(TestCase):

    def test_1_sum(self):
        self.assertEqual(adding_sum(4, 5), 9)

    def test_3_valid_sum(self):
        self.assertEqual(adding_sum(3, 4), 7)
