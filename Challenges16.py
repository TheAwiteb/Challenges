#Friday the 13th

#Given the month and year as numbers, return whether that month contains a Friday 13th.

##Examples

    #has_friday_13(3, 2020) ➞ True

    #has_friday_13(10, 2017) ➞ True

    #has_friday_13(1, 1985) ➞ False

#Notes

    #January will be given as 1, February as 2, etc ...

import datetime

def has_friday_13(month, year):
    day_name = datetime.date(int(year), int(month), 13)
    day_name = (day_name.strftime("%A"))
    if day_name == "Friday":
        return True
    else:
        return False