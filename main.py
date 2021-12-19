from FlipCoin import FlipCoin
from LeapYear import LeapYear
# Added a program of Flip Coin
import LeapYear


class BasicCore:
    def __init__(self):
        print("Please Enter Your Choice")
        basic_core_programs = {1: 'Flip Coin', 2: 'Leap Year'}
        print(basic_core_programs)
        choice = int(input("Enter Your Choice"))
        if choice == 1:
            FlipCoin.flip_coin_fun("Enter The Times")
        elif choice == 2:
            LeapYear.leap_year("Enter The Year")
        else:
            print("Wrong Choice")


welcome = BasicCore.__init__("Welcome")
print(welcome)
