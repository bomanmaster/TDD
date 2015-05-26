__author__ = 'Konrad'

import unittest
import aplikacja

class Test_sum_of_squares_diffrence(unittest.TestCase):

    def test_sum_of_squares_(self):
        self.assertEqual(aplikacja.Sum_of_squares_diffrence.sum_squares(self), 385)



suite = unittest.TestLoader().loadTestsFromTestCase(Test_sum_of_squares_diffrence)
unittest.TextTestRunner(verbosity=2).run(suite)


