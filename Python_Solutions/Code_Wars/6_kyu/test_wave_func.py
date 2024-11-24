from unittest import TestCase
from wave_func import wave

class TestWaveFunc(TestCase):

    def test_normal_wave(self):
        result = wave("mood")
        self.assertEqual(result, ['Mood', 'mOod', 'moOd', 'mooD'])

    def test_numerical_wave(self):
        result = wave("1234")
        self.assertEqual(result, [])

    def test_upper_wave(self):
        result = wave("CAPITAL")
        self.assertEqual(result, [['CAPITAL', 'CAPITAL', 'CAPITAL', 'CAPITAL', 'CAPITAL', 'CAPITAL', 'CAPITAL']])