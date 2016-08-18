#usr/bin/python
import unittest
from sum import my_sum

class MySumTests(unittest.TestCase):
    def setUp(self):
        self.numbers = [10,5,7,8,90]
    def	test_sum_of_digits(self):
        '''
    test sum of digits/number
        '''
        result = my_sum(5,10)
        self.assertEqual(result,15,'test faild testcase 5 + 10')
        self.assertEqual(my_sum(10,15),25)
    def test_none_numbers(set):
        result = my(8,7)
        self.assert
if __name__ =='__main__':
   unittest.main() 
