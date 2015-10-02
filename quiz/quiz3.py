#!/usr/bin/env python

'''
Spark-Training Enterance quizzes.
'''
import unittest


# 1: reverse a string
def reverse_string_a(s):
    return s[::-1]


def reverse_string_b(s):
    return ''.join(reversed(s))


# 2: Reverse a sentence ("bob likes dogs" -> "dogs likes bob")
def reverse_sentence(sentence):
    return ' '.join(reversed(sentence.split()))


# 3: Find the maximum value in a list
def find_max(my_list):
    _max = 0
    for num in my_list:
        _max = num if num > _max else _max
    return _max


# 4: Calculate a remainder (given a numerator and denominator)
def get_remainder_a(numerator, denominator):
    return numerator % denominator


def get_remainder_b(numerator, denominator):
    '''
    works only on python 2.X
    makes use of integer divison.
    '''
    return numerator - (numerator/denominator) * denominator


# 5: Return distinct values from a list including duplicates (i.e. "1 3 5 3 7 3 1 1 5" -> '1 3 5 7')
def get_distinct_a(values):
    distinct = []
    for value in values:
        distinct.append(value) if value not in distinct else ''

    return distinct


def get_distinct_b(values):
    return list(set(values))


# ################# # ###  TESTS ##### # ##########################

class QuizTest(unittest.TestCase):

    def test_1_a(self):
        my_test_string = 'Spark'
        should_be = 'krapS'
        res = reverse_string_a(my_test_string)
        self.assertEqual(res, should_be)
        print("Successfully finished quiz 1.")

    def test_1_b(self):
        my_test_string = 'Spark'
        should_be = 'krapS'
        res = reverse_string_b(my_test_string)
        self.assertEqual(res, should_be)
        print("Successfully finished quiz 1.")

    def test_2(self):
        test_sentence = 'bob likes dogs'
        should_be = 'dogs likes bob'
        res = reverse_sentence(test_sentence)
        self.assertEqual(res, should_be)
        print("Successfully finished quiz 2.")

    def test_3(self):
        res = find_max([1, 2, 34, 3453, 32412, 123, 44])
        should_be = 32412
        self.assertEqual(res, should_be)
        print("Successfully finished quiz 3.")

    def test_4_a(self):
        res = get_remainder_a(5, 2)
        should_be = 1
        self.assertEqual(res, should_be)
        print("Successfully finished quiz 4.")

    def test_4_b(self):
        res = get_remainder_b(5, 2)
        should_be = 1
        self.assertEqual(res, should_be)
        print("Successfully finished quiz 4.")

    def test_5_a(self):
        res = get_distinct_a([1, 2, 333, 333, 333, 22, 2, 35, 1, 66])
        should_be = [1, 2, 333, 22, 35, 66]
        self.assertEqual(res, should_be)
        print("Successfully finished quiz 5.")

    def test_5_b(self):
        res = get_distinct_a([1, 2, 333, 333, 333, 22, 2, 35, 1, 66])
        should_be = [1, 2, 333, 22, 35, 66]
        self.assertEqual(res, should_be, )
        print("Successfully finished quiz 5.")

if __name__ == '__main__':
    unittest.main()
