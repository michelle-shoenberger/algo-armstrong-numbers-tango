# The code is written as driver code. Can you convert it to Unit Test?
import unittest
import armstrong_numbers 

class ArmstrongTester(unittest.TestCase):

    test_numbers = [0, 25, 100, 153, 371, 999]
    single_number = [5]
    double_numbers = [12, 25, 75]

    def test_return(self):
        """ This tests that function returns a value"""
        self.assertIsNotNone(armstrong_numbers.find_armstrong_numbers(self.test_numbers))

    def test_single_digit(self):
        """Tests that a single digit number returns the number"""
        self.assertEqual(armstrong_numbers.find_armstrong_numbers(self.single_number), self.single_number)

    def test_second_digit(self):
        """Tests that double digit returns correctly, not Arm numbers"""
        self.assertEqual(armstrong_numbers.find_armstrong_numbers(self.double_numbers), [])
    def test_triple_digit(self):
        """Tests that triple digit returns correctly"""
        self.assertEqual(armstrong_numbers.find_armstrong_numbers(self.test_numbers), [0, 153, 371])

    

if __name__ == "__main__":
    unittest.main()



# print(find_armstrong_numbers([0]) == [0]) 
# print(find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7])
# print(find_armstrong_numbers(list(range(0,100))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(find_armstrong_numbers(list(range(0,999))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
