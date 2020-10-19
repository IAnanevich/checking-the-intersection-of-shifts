"""
Есть 2 рабочие смены через класс:

class Shift:
    time_from: time
    time_to: time
    date_from: date
    date_to: date
    week_days: list

Нужно проверить, что они не пересекают друг друга
"""
from datetime import date, time, timedelta
from typing import Tuple


def add_days(days_week: list, time_to: timedelta, time_from: timedelta, date_to: date) -> Tuple:
    """
    Add days to week_days
    :param days_week: week days
    :param time_to: shift end time
    :param time_from: shift start time
    :param date_to: end date of shifts
    :return: new days week
    """
    for day in set(days_week):
        if time_from > time_to:
            if not (day + 1 in days_week):
                days_week.append(day + 1)
                date_to += timedelta(days=1)
    return days_week, date_to


class Shift:
    """
    The class allows you to work with shifts.
    """

    def __init__(
            self,
            time_from: time,
            time_to: time,
            date_from: date,
            date_to: date,
            week_days: list,
    ):
        """
        Constructor of our class
        :param time_from: shift start time
        :param time_to: shift end time
        :param date_from: start date of shifts
        :param date_to: end date of shifts
        :param week_days: week days
        """
        self.time_from = time_from
        self.time_to = time_to
        self.date_from = date_from
        self.date_to = date_to
        self.week_days = week_days

    @staticmethod
    def compare(self, other) -> bool:
        """
        Compare 2 shifts
        :param self: first shift
        :param other: second shift
        :return: true or false
        """
        from_time_1 = timedelta(
            hours=self.time_from.hour, minutes=self.time_from.minute, seconds=self.time_from.second
        )

        to_time_1 = timedelta(
            hours=self.time_to.hour, minutes=self.time_to.minute, seconds=self.time_to.second
        )

        from_time_2 = timedelta(
            hours=other.time_from.hour, minutes=other.time_from.minute, seconds=other.time_from.second
        )

        to_time_2 = timedelta(
            hours=other.time_to.hour, minutes=other.time_to.minute, seconds=other.time_to.second
        )

        self.week_days, self.date_to = add_days(self.week_days, to_time_1, from_time_1, self.date_to)
        other.week_days, other.date_to = add_days(other.week_days, to_time_2, from_time_2, other.date_to)

        for day in self.week_days:
            if day in other.week_days:
                if (self.date_from <= other.date_from <= self.date_to
                        or other.date_from <= self.date_from <= other.date_to):
                    if (self.time_from <= other.time_from < self.time_to
                            or other.time_from < self.time_from < other.time_to):
                        return True
                    if self.time_from > self.time_to or other.time_from > other.time_to:
                        if self.time_from < other.time_to or other.time_from < self.time_to:
                            return True
        return False
