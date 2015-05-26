__author__ = 'Konrad'

import unittest
import aplikacja

class Test_sum_of_squares_diffrence(unittest.TestCase):

    def test_sum_squares(self):
        self.assertEqual(aplikacja.Sum_of_squares_diffrence.sum_squares(self), 385)

    def test_square_sum(self):
        self.assertEqual(aplikacja.Sum_of_squares_diffrence.square_sum(self), 3025)

    def test_subtract(self):
        self.assertEqual(aplikacja.Sum_of_squres_diffrence.subtract(self,385,3025), 2640)    



suite = unittest.TestLoader().loadTestsFromTestCase(Test_sum_of_squares_diffrence)
unittest.TextTestRunner(verbosity=2).run(suite)


