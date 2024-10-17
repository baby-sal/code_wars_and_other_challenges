
from unittest import TestCase
from mini_mock_q2 import total_revenue

class TestTotalRevFunc(TestCase):

    def test_normal_dict(self):
        result = total_revenue({
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.7,
    "grape": 1.2
},{
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 12
}, )
        self.assertEqual(result, 26.5)


    def test_large_number_dict(self):
        result = total_revenue({
    "apple": 500,
    "banana": 300,
    "orange": 700,
    "grape": 1200
},{
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 12
}, )
        self.assertEqual(result, 26500)

