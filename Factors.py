import math


class PrimeFactors:
    """Here We Are checking the prime factors of all the numbers that
        is entered by the user by the formula i*i<=number"""
    def primefactors(self):
        number = int(input("Enter A Number Whose Prime Factors You Want"))
        if number > 0:
            while number %2 == 0:
                print(2)
                number = number / 2
                for i in range(3,int(math.sqrt(number))+1,2):
                    while number % i == 0:
                        print(i)
                        number = number/i
                if number > 2:
                    print(number)

