from datetime import time


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        current_time = time(self.hours, self.minutes, self.seconds)
        return f"{current_time.strftime('%H:%M:%S')}"

    def next_second(self):
        self.seconds += 1
        if Time.max_seconds < self.seconds:
            self.minutes += 1
            self.seconds = 0
        if Time.max_minutes < self.minutes:
            self.hours += 1
            self.minutes = 0
        if Time.max_hours < self.hours:
            self.hours = 0
        return self.get_time()


time_1 = Time(9, 30, 59)
print(time_1.next_second())
time_2 = Time(10, 59, 59)
print(time_2.next_second())
time_3 = Time(23, 59, 59)
print(time_3.next_second())
