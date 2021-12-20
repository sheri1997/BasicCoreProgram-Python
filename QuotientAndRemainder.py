class QuotientAndRemainder:
    """In this program we are calculating the simple
        quotient and remainder using simple mathematics rule"""
    def quotient_and_remainder(self):
        dividend = int(input("Enter The Dividend value"))
        divisor = int(input("Enter The Divisor value"))
        quotient = dividend / divisor
        remainder = dividend % divisor
        print("Quotient : ", quotient)
        print("Remainder : ", remainder)
