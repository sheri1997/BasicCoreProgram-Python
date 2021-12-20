class Largest:
    def largest(self):
        number1 = int(input("Enter The First Number"))
        number2 = int(input("Enter The Second Number"))
        number3 = int(input("Enter The Third Number"))
        if number1 > number2 and number1 > number3:
            print("first number is the greatest")
        elif number2 > number1 and number2 > number3:
            print("second number is the greatest")
        else:
            print("third number is the greatest")
