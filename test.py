import unittest
from ijones import IJones
from reader import read_plate_file



class MyTestCase(unittest.TestCase):
    def test_ex_1(self):
        input_file_params = read_plate_file("ex_1.txt")
        self.assertEqual(IJones(*input_file_params), 5)

    def test_ex_2(self):
        input_file_params = read_plate_file("ex_2.txt")
        self.assertEqual(IJones(*input_file_params), 2)

    def test_ex_3(self):
        input_file_params = read_plate_file("ex_3.txt")
        self.assertEqual(IJones(*input_file_params), 201684)


if __name__ == '__main__':
    unittest.main()