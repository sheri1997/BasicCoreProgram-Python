import calendar


class LeapYear:
    """Here We are calling the calendar class
        to check whether the input number is leap or not
        the calendar.isleap(year) method will return true
        if it is leap year else will return false"""
    def leap_year(self):
        leap_input = int(input("Enter The Year For Which You Want To Check The Leap Year :"))
        leap = calendar.isleap(leap_input)
        if leap:
            print("Leap Year")
        else:
            print("Not A Leap Year")

