import sys
import unittest

sys.path.append('..')


import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_generate(self):
        expectation = [
            '1', '2', 'fizz', '4', 'buzz',
            'fizz', '7', '8', 'fizz', 'buzz',
            '11', 'fizz', '13', '14', 'fizzbuzz',
        ]
        self.assertEqual(fizzbuzz.generate(15), expectation)


class TestNumber(unittest.TestCase):
    def test_negative_number(self):
        """_Number doesn't allow negative numbers"""
        with self.assertRaises(ValueError):
            fizzbuzz._Number(-5)

    def test_fizz_number(self):
        """_Number stringifies as 'fizz' when divisible by 3"""
        for i in [3, 6, 333]:
            n = fizzbuzz._Number(i)
            self.assertEqual(str(n), 'fizz')

    def test_is_fizz(self):
        """_Number.is_fizz()"""
        self.assertTrue(fizzbuzz._Number(0).is_fizz())
        self.assertTrue(fizzbuzz._Number(3).is_fizz())
        self.assertTrue(fizzbuzz._Number(15).is_fizz())
        self.assertFalse(fizzbuzz._Number(5).is_fizz())

    def test_buzz_number(self):
        """_Number stringifies as 'buzz' when divisible by 3"""
        for i in [5, 10, 500]:
            n = fizzbuzz._Number(i)
            self.assertEqual(str(n), 'buzz')

    def test_is_buzz(self):
        """_Number.is_buzz()"""
        self.assertTrue(fizzbuzz._Number(0).is_buzz())
        self.assertTrue(fizzbuzz._Number(5).is_buzz())
        self.assertTrue(fizzbuzz._Number(15).is_buzz())
        self.assertFalse(fizzbuzz._Number(3).is_buzz())

    def test_fizzbuzz_number(self):
        """_Number stringifies as 'fizzbuzz' when divisible by 3 and 5"""
        for i in [0, 15, 225]:
            n = fizzbuzz._Number(i)
            self.assertTrue(n.is_fizzbuzz())
            self.assertEqual(str(n), 'fizzbuzz')

    def test_is_fizzbuzz(self):
        """_Number.is_fizzbuzz()"""
        self.assertTrue(fizzbuzz._Number(0).is_fizzbuzz())
        self.assertTrue(fizzbuzz._Number(15).is_fizzbuzz())
        self.assertFalse(fizzbuzz._Number(5).is_fizzbuzz())
        self.assertFalse(fizzbuzz._Number(3).is_fizzbuzz())

    def test_non_fizzbuzz_number(self):
        """_Number stringifies as the number when not divisible by 3 nor 5"""
        for i in [2, 13, 1001]:
            n = fizzbuzz._Number(i)
            self.assertFalse(n.is_fizz())
            self.assertFalse(n.is_buzz())
            self.assertFalse(n.is_fizzbuzz())
            self.assertEqual(str(n), str(i))


if __name__ == '__main__':
    unittest.main()
