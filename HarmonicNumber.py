class HarmonicNumber:
    """Here We are Calculating the Nth Harmonic Number of the Number Enterd
        by the user by the Formula (1/1)+(1/2)+....(1/Number)
        The Number Entered by the user should be positive"""
    def harmonic(self):
        value = 1.0
        harmonic_number = int(input("Enter A Number"))
        if harmonic_number >0:
            harmoniousness = harmonic_number+1
            for i in range(1,harmoniousness):
                value = value + (1/harmonic_number)
        print("Harmonic Number : ",value)


