from Codewars_practice.solutions import *
import unittest


class SampleTest(unittest.TestCase):

    def test_dubstep_test(self):
        expected_result = "A B C"
        self.assertEqual(expected_result, song_decoder("AWUBBWUBC"))
        self.assertEqual(expected_result, song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
        self.assertEqual(expected_result, song_decoder("WUBAWUBBWUBCWUB"))

    def test_find_next_square(self):
        self.assertEqual(-1, find_next_square(155), "Wrong")
        self.assertEqual(-1, find_next_square(342786627))
        self.assertEqual(144, find_next_square(121))
        self.assertEqual(676, find_next_square(625))

    def test_is_triangle(self):
        self.assertEqual(True, is_triangle(1, 2, 2))
        self.assertEqual(False, is_triangle(7, 2, 2))

    def test_to_camel_case(self):
        self.assertEqual("theStealthWarrior", to_camel_case("A_Pippi_Is-Omoshiroi"))

    def test_divisors(self):
        self.assertEqual([3, 5], divisors(15))
        self.assertEqual([2, 3, 4, 6], divisors(12))
        self.assertEqual("13 is prime", divisors(13))
