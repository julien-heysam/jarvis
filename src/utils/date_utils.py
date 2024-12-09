import math
from datetime import date, datetime, timedelta


class DateUtils:
    @staticmethod
    def readable_today_date() -> str:
        """
        Returns the current date in a readable format with day, month, and year.
        """
        return datetime.now().strftime("%d %B %Y")

    @staticmethod
    def str_to_datetime(str_date: str) -> date:
        """
        Converts a string representation of a date in the format "YYYY-MM-DD" to a `date` object.
        """
        return datetime.strptime(str_date, "%Y-%m-%d").date()

    @staticmethod
    def seconds_to_min_sec(seconds: float) -> str:
        """
        Converts a given number of seconds into minutes and seconds in the format "minutes:seconds".
        """
        minutes, sec = divmod(int(seconds), 60)
        return f"{minutes:02}:{sec:02}"

    @staticmethod
    def datetime_difference(date1: date, date2: date, how: str = "months") -> int:
        """
        Calculates the difference between two dates in either days, months, or years.
        """
        if not date1 or not date2:
            return None
        days = abs((date2 - date1).days)

        match how:
            case "days":
                return days
            case "months":
                return days // 30
            case "years":
                return days // 360
            case _:
                return days

    @staticmethod
    def months_until_date(dt: str) -> int:
        """
        Calculates the number of months until a specified date.
        """
        today = datetime.today()
        months = math.ceil((datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S") - today).days / 30)
        return months

    @staticmethod
    def get_first_day_of_month(input_date: date = None) -> date:
        """Returns the first day of the month for a given date."""
        input_date = input_date or datetime.now().date()
        return input_date.replace(day=1)

    @staticmethod
    def get_last_day_of_month(input_date: date = None) -> date:
        """Returns the last day of the month for a given date."""
        input_date = input_date or datetime.now().date()
        next_month = input_date.replace(day=28) + timedelta(days=4)
        return next_month - timedelta(days=next_month.day)

    @staticmethod
    def is_weekend(input_date: date = None) -> bool:
        """Returns True if the date is a weekend (Saturday or Sunday)."""
        input_date = input_date or datetime.now().date()
        return input_date.weekday() >= 5

    @staticmethod
    def add_business_days(input_date: date, days: int) -> date:
        """
        Add business days to a date, skipping weekends.
        Positive days moves forward, negative days moves backward.
        """
        input_date = input_date or datetime.now().date()
        current_date = input_date
        remaining_days = days
        
        while remaining_days != 0:
            step = 1 if remaining_days > 0 else -1
            current_date += timedelta(days=step)
            if not DateUtils.is_weekend(current_date):
                remaining_days -= step
                
        return current_date

    @staticmethod
    def format_relative_date(input_date: date) -> str:
        """
        Returns a human-readable relative date string (e.g., 'today', 'yesterday', '2 days ago').
        """
        today = datetime.now().date()
        delta = (today - input_date).days

        if delta == 0:
            return "today"
        elif delta == 1:
            return "yesterday"
        elif delta == -1:
            return "tomorrow"
        elif delta > 1:
            return f"{delta} days ago"
        else:
            return f"in {abs(delta)} days"

if __name__ == "__main__":
    print(DateUtils.months_until_date("2023-10-25T00:00:00"))
