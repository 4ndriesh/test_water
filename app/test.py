import unittest
import numpy as np
from matrix import Matrix

class TestWaters(unittest.TestCase):
    def test_upper(self):
        matrix = Matrix()
        matrix.get_obj_with_water = np.array([[1, 1, 1, 0, 0],
                                              [1, 1, 0, 0, 0],
                                              [1, 1, 1, 1, 0],
                                              [1, 1, 0, 0, 0],
                                              [1, 1, 1, 1, 0]])
        self.assertEqual(matrix.get_obj_with_water,  [[1, 1, 1, 0, 0],
                                                      [1, 1, 31, 0, 0],
                                                      [1, 1, 1, 1, 0],
                                                      [1, 1, 33, 23, 0],
                                                      [1, 1, 1, 1, 0]])

        matrix.get_obj_with_water = np.array([[1, 1, 1, 0, 0],
                                            [1, 1, 0, 0, 0],
                                            [1, 0, 0, 0, 0],
                                            [1, 1, 0, 0, 0],
                                            [1, 1, 1, 1, 0]])
        self.assertEqual(matrix.get_obj_with_water,[[1, 1, 1, 0, 0],
                                                     [1, 1, 31, 0, 0],
                                                     [1, 42, 31, 0, 0],
                                                     [1, 1, 31, 0, 0],
                                                     [1, 1, 1, 1, 0]])

if __name__ == '__main__':
    unittest.main()
