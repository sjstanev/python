class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int) -> None:
        """
        update the time with the new values
        :param hours:
        :param minutes:
        :param seconds:
        :return:
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self)  -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self) -> str:
        """
        time = Time(25, 63, 74)
        print(time.next_second())
        if there are WRONG inputs in seconds parameters = 74
        # >>> 74 // 60 = 1 increase with one minutes            1
        # >>> 74 % 60 = 14 remaining seconds are

        :return:
        """
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds %= 60 # >>> 74 % 60 = 14 remaining seconds are
            self.minutes  += 1
        if self.minutes > Time.max_minutes:
            self.minutes %= 60 # >>> 63 % 60 = 3 remaining minutes are
            self.hours += 1
        if self.hours > Time.max_hours:
            self.hours %= 24
        return self.get_time()


time = Time(25, 63, 74)
print(time.next_second())
time = Time(25, 5, 74)
print(time.next_second())
time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())