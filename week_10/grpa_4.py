"""
Create a class Time with the following specification:

Attributes
time: int, represents time in seconds

Methods
    (1) __init__: accept time in seconds as an argument and assign it to the
corresponding attribute
    (2) seconds_to_minutes: convert the value of time into minutes and return a
string in the format: "<minutes> min <seconds> sec". For example: if the
value of the attribute time is 170170, this method should return the string
"2 min 50 sec"

    (3) seconds_to_hours: convert the value of time into hours and return a
string in the format: "<hours> hrs <minutes> min <seconds> sec".
For example: if the value of the attribute time is 1089010890, this method
should return the string "3 hrs 1 min 30 sec"

    (4) seconds_to_days: convert the value of time into days and return a
string in the format: "<days> days <hours> hrs <minutes> min <seconds> sec".
For example: if the value of the attribute time is 8646086460, this method
should return the string "1 days 0 hrs 1 min 0 sec"
"""


class Time():
    def __init__(self, time):
        self.time = time

    def seconds_to_minutes(self):
        min = self.time // 60
        sec = self.time % 60
        return f"{min} min {sec} sec"

    def seconds_to_hours(self):
        hour = self.time // 3600
        remaining_sec = self.time % 3600
        min = remaining_sec // 60
        sec = remaining_sec % 60
        return f"{hour} hrs {min} min {sec} sec"

    def seconds_to_days(self):
        day = self.time // 86400
        remaining_sec_1 = self.time % 86400
        hour = remaining_sec_1 // 3600
        remaining_sec_2 = remaining_sec_1 % 3600
        min = remaining_sec_2 // 60
        sec = remaining_sec_2 % 60
        return f"{day} days {hour} hrs {min} min {sec} sec"
