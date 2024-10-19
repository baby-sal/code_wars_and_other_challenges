from unittest import TestCase
from warmup import dash_func

class TestDashFunc(TestCase):

    def test_normal_string(self):
        result = dash_func("Sally")
        self.assertEqual(result,"S-a-l-l-y")

        # self.assertEqual(dash_func("Sally"), "S-a-l-l-y")

    def test_empty_string(self):
        result = dash_func(" ")
        self.assertEqual(result, " ")


    def test_numbers_string(self):
        result = dash_func("123456789")
        self.assertEqual(result, "1-2-3-4-5-6-7-8-9")


    def test_special_char(self):
        result = dash_func("*&^$")
        self.assertEqual(result, "*-&-^-$")

