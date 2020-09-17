import unittest
from shift_time import Shift
from data_time import tests_false, tests_true


class ShiftTest(unittest.TestCase):
    def test_good(self):
        shift_list, check_list = [], []
        for shifts in tests_true:
            shift1 = Shift(
                time_from=shifts[0]["time_from"],
                time_to=shifts[0]["time_to"],
                date_from=shifts[0]["date_from"],
                date_to=shifts[0]["date_to"],
                week_days=shifts[0]["week_days"]
            )
            shift2 = Shift(
                time_from=shifts[1]["time_from"],
                time_to=shifts[1]["time_to"],
                date_from=shifts[1]["date_from"],
                date_to=shifts[1]["date_to"],
                week_days=shifts[1]["week_days"]
            )
            shift_list.append(Shift.compare(shift1, shift2))
            check_list.append(True)

        self.assertEqual(shift_list, check_list)

    def test_bad(self):
        shift_list, check_list = [], []
        for shifts in tests_false:
            shift1 = Shift(
                time_from=shifts[0]["time_from"],
                time_to=shifts[0]["time_to"],
                date_from=shifts[0]["date_from"],
                date_to=shifts[0]["date_to"],
                week_days=shifts[0]["week_days"]
            )
            shift2 = Shift(
                time_from=shifts[1]["time_from"],
                time_to=shifts[1]["time_to"],
                date_from=shifts[1]["date_from"],
                date_to=shifts[1]["date_to"],
                week_days=shifts[1]["week_days"]
            )
            shift_list.append(Shift.compare(shift1, shift2))
            check_list.append(False)

        self.assertEqual(shift_list, check_list)


if __name__ == '__main__':
    unittest.main()
