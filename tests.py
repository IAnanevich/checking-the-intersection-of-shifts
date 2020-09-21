import unittest
from shift_time import Shift
from data_time import tests_false, tests_true
from ddt import ddt, unpack, data


@ddt
class ShiftTest(unittest.TestCase):

    @data(tests_false)
    @unpack
    def test_1(self, tuple1, tuple2):
        @data(tuple1, tuple2)
        @unpack
        def test_bad(shift_1, shift_2):
            self.assertFalse(Shift.compare(shift_1, shift_2))

    @data(tests_true)
    @unpack
    def test_2(self, *args):
        @data(*args)
        @unpack
        def test_good(shift_1, shift_2):
            self.assertTrue(Shift.compare(shift_1, shift_2))


if __name__ == '__main__':
    unittest.main()
