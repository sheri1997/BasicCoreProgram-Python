from FlipCoin import FlipCoin
from LeapYear import LeapYear
from PowerOf2 import PowerOf2
from HarmonicNumber import HarmonicNumber
from Factors import PrimeFactors
from QuotientAndRemainder import QuotientAndRemainder
from SwapTwoNumbers import SwapTwoNumbers

'''It contains the basic core programs
    the choices are being stored in the dictionary'''


class BasicCore:
    def basic(self):
        print("Please Enter Your Choice")
        basic_core_programs = {1: 'Flip Coin', 2: 'Leap Year', 3: 'Power Of 2', 4: 'Harmonic Number',
                               5: 'Prime Factors', 6: 'Quotient And Remainder', 7: 'Swap Two Numbers'}
        print(basic_core_programs)
        choice = int(input("Enter Your Choice"))
        if choice == 1:
            FlipCoin.flip_coin_fun("Enter The Times")
        elif choice == 2:
            LeapYear.leap_year("Enter The Year")
        elif choice == 3:
            PowerOf2.power("Enter The Number")
        elif choice == 4:
            HarmonicNumber.harmonic("Enter The Number")
        elif choice == 5:
            PrimeFactors.primefactors("Enter The Number")
        elif choice == 6:
            QuotientAndRemainder.quotient_and_remainder("Enter The Number")
        elif choice == 7:
            SwapTwoNumbers.swap("Enter The Numbers")
        else:
            print("Wrong Choice")


welcome = BasicCore.basic("Welcome")
print(welcome)
