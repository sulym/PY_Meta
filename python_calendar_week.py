from datetime import datetime, timedelta


def calendar_week(date_string: str) -> int:
    date = datetime.strptime(date_string, "%Y-%m-%d")
    year_start = datetime(date.year, 1, 1)
    if year_start.weekday() > 3:
        year_start += timedelta(7 - year_start.weekday())
    else:
        year_start -= timedelta(year_start.weekday())
    week_start = year_start
    if date < week_start:
        week_start -= timedelta(weeks=1)
    week_number = int(((date - week_start).days // 7) + 1)
    if week_number == 0:
        if week_start.year != date.year:
            week_number = 53
        else:
            week_number = 1
    return week_number


### m ###

from datetime import datetime


def calendar_week(date_string: str) -> int:
    return datetime.strptime(date_string, "%Y-%m-%d").isocalendar()[1]


