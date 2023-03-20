from typing import Union


weekdays = ["Wednesday", "Monday", "Saturday"]
def weekday_order(weekday: str) -> int:
    # write your code here
    if weekday == "Monday":
        return 1
    if weekday == "Tuesday":
        return 2
    if weekday == "Wednesday":
        return 3
    if weekday == "Thursday":
        return 4
    if weekday == "Friday":
        return 5
    if weekday == "Saturday":
        return 6
    if weekday == "Sunday":
        return 7

def sort_weekdays(weekdays: list) -> list:
    # write your code here
    return sorted(weekdays, key=weekday_order)

print(sort_weekdays(weekdays))