from unittest import TestCase
from palindrome_tasks import palindrome_check

class TestPalindromeFunc(TestCase):

    def test_normal_palindrome(self):
        result = palindrome_check("anna")
        self.assertEqual(result, True)

    def test_numerical_palindrome(self):
        result = palindrome_check("1221")
        self.assertEqual(result, True)

    def test_special_palindrome(self):
        result = palindrome_check("+==+")
        self.assertEqual(result, True)

    def test_not_palindrome(self):
        result = palindrome_check("1234")
        self.assertFalse(result)#checks that there is False result