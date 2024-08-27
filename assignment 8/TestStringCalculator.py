from string_calculator import *
import unittest

class TestStringCalculator(unittest.TestCase):
    SC=StringCalculator()

    def test_two_positive_numbers(self):
        self.assertEqual(self.SC.add('5,6'),11)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            self.SC.add('-5,6')

    def test_larger_than_1_digit_numbers(self):
        self.assertEqual(self.SC.add('50,655'),705)

    def test_empty_string(self):
        self.assertEqual(self.SC.add(''), 0)
        
    # def test_non_numerics(self):
    #     with self.assertRaises(ValueError):
    #         self.SC.add('t,r')

    def test_custom_delimiters(self):
        self.assertEqual(self.SC.add('//[*]\n50*655*20'),725)

    def test_huge_numbers(self):
        self.assertEqual(self.SC.add('50,65655'),50)

    def test_single_number(self):
        self.assertEqual(self.SC.add('5'),5)

   # def test_custom_delimiters_at_end(self):
   #     self.assertEqual(self.SC.add('50*655*20//[*]\n'),725)

  #  def test_non_numeric(self):
  #       with self.assertRaises(ValueError):
   #          self.SC.add('t,5')


    def test_lots_of_numbers(self):
        self.assertEqual(self.SC.add('5,6,7,6,8,5,8,23'),68)
if __name__ == '__main__':
    unittest.main()

print(SC.add('5,6'))
