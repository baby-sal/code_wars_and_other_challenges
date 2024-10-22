from unittest import TestCase
from cylinder_challenge import water_volume, NegativeValue


class TestWaterVolumeFunc(TestCase):

    def test_normal_volume(self):
        result = water_volume(3,4)
        self.assertEqual(result, 113.09733552923255)

    def test_large_volume(self):
        result = water_volume(323454,34567)
        self.assertEqual(result, 1.1361524642535386e+16)

    def test_same_radius_same_height(self):
        result = water_volume(1,1)
        self.assertEqual(result, 3.141592653589793)

    def test_negative_height(self):
        with self.assertRaises(NegativeValue):
            water_volume(1,-3)
