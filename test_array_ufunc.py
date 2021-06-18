import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArrayUfunc(unittest.TestCase):

    def test_abs(self):
        vector = np.array([-1, 1, -7])
        assert_array_equal(np.abs(vector), np.array([1, 1, 7]))

    def test_sqrt(self):
        vector = np.array([9, 16, 25])
        assert_array_equal(np.sqrt(vector), np.array([3, 4, 5]))

    def test_sort(self):
        vector = np.array([1, 6, 2, 3, 8, 1])
        assert_array_equal(np.sort(vector), np.array([1, 1, 2, 3, 6, 8]))

    def test_argsort(self):
        vector = np.array([2, 6, 1])
        assert_array_equal(np.argsort(vector), np.array([2, 0, 1]))

    def test_add(self):
        A = np.array([0, 1, 2])
        B = np.array([2, -1, 4])
        assert_array_equal(np.add(A, B), np.array([2, 0, 6]))

    def test_subtract(self):
        A = np.array([0, 1, 2])
        B = np.array([2, -1, 4])
        assert_array_equal(np.subtract(A, B), np.array([-2, 2, -2]))

    def test_maximum(self):
        A = np.array([0, 1, 2])
        B = np.array([2, -1, 4])
        assert_array_equal(np.maximum(A, B), np.array([2, 1, 4]))

if __name__ == '__main__':
    unittest.main()