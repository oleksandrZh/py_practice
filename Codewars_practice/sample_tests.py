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

    def test_decrypt(self):
        self.assertEqual("This is a test!", )

    def test_encrypt(self):
        self.assertEqual("hsi  etTi sats!", encrypt("This is a test!", 1), "First")
        self.assertEqual("This is a test!", encrypt("This is a test!", 0), "Second")
        self.assertEqual("s eT ashi tist!", encrypt("This is a test!", 2), "Third")
        self.assertEqual(" Tah itse sits!", encrypt("This is a test!", 3), "3")
        self.assertEqual("This is a test!", encrypt("This is a test!", 4), "4")

    def test_decrypt(self):
        self.assertEqual("This is a test!", decrypt("This is a test!", 0), "0")
        self.assertEqual("This is a test!", decrypt("hsi  etTi sats!", 1), "1")
        self.assertEqual("This is a test!", decrypt("s eT ashi tist!", 2), "2")

    def test_nb_year(self):
        self.assertEqual(15, nb_year(1500, 5, 100, 5000))
        self.assertEqual(10, nb_year(1500000, 2.5, 10000, 2000000))
        self.assertEqual(94, nb_year(1500000, 0.25, 1000, 2000000))

    def test_is_prime(self):
        self.assertEqual(False, is_prime(0))
        self.assertEqual(False, is_prime(1))
        self.assertEqual(True, is_prime(2))
        self.assertEqual(False, is_prime(4))

    def test_duplicate_count(self):
        self.assertEqual(0, duplicate_count("abcde"))
        self.assertEqual(1, duplicate_count("abcdea"))
        self.assertEqual(1, duplicate_count("indivisibility"))
        self.assertEqual(2, duplicate_count("Indivisibilities"))
        self.assertEqual(2, duplicate_count("aabbcde"))
        self.assertEqual(2, duplicate_count("aabBcde"))

    def test_anagrams(self):
        self.assertEqual(['aabb', 'bbaa'], anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

    def test_cakes(self):
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        self.assertEqual(2, cakes(recipe, available))

        recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available = {"sugar": 500, "flour": 2000, "milk": 2000}
        self.assertEqual(0, cakes(recipe, available))

    def test_find_missings(self):
        self.assertEqual(5, find_missing([1, 2, 3, 4, 6, 7, 8, 9]))
        self.assertEqual(2, find_missing([1, 3, 4, 5, 6, 7, 8, 9]))
        self.assertEqual(7, find_missing([1, 3, 5, 9, 11]))

    def test_rgb(self):
        self.assertEqual("000000", rgb(0, 0, 0))
        self.assertEqual("010203", rgb(1, 2, 3))
        self.assertEqual("FFFFFF", rgb(255, 255, 255))
        self.assertEqual("FEFDFC", rgb(254, 253, 252))
        self.assertEqual("00FF7D", rgb(-20, 275, 125))
