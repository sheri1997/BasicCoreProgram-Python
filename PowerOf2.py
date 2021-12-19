class PowerOf2:
    """in this program we are calculting the power of two
        for the number which the user is entering
        by using the pow() function."""
    def power(self):
        number = int(input("Enter The Number"))
        power_of_two = pow(number,2)
        print("Power of Two for ",number," is ",power_of_two)



