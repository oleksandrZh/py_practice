from Application.math_methods import *
from Application.str_methods import *
import unittest


class MathTests(unittest.TestCase):

    def setUp(self):
        print("start test")

    def test_plus_2_args(self):
        arg1 = 1
        arg2 = 2
        sum = plus(arg1 + arg2)
        self.assertEqual(3, sum)

    def test_plus_3_args(self):
        arg1 = 1
        arg2 = 2
        arg3 = 3
        sum = plus(arg1 + arg2 + arg3)
        self.assertEqual(6, sum)

    def test_plus_4_args(self):
        arg1 = 1
        arg2 = 2
        arg3 = 3
        arg4 = 4
        sum = plus(arg1 + arg2 + arg3 + arg4)
        self.assertEqual(10, sum)


class StrMethodsTest(unittest.TestCase):
    def test_word_count_method(self):
        args2 = "Two word"
        args3 = "Three simple word"
        self.assertEqual(2, count_words(args2))
        self.assertEqual(3, count_words(args3))

    def test_create_hokku_test(self):
        args1 = "Tests were created"
        args2 = "for managers"
        args3 = "by brave QAs"
        args4 = "wrong hokku"
        expected_result = args1 + "\n" + args2 + "\n" + args3
        self.assertEqual(expected_result, create_hokku(args1, args2, args3))
        expected_result = expected_result + "\n" + args4
        self.assertEqual(expected_result, create_hokku(args1, args2, args3, args4))
