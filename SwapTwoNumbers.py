class SwapTwoNumbers:
    def swap(self):
        number_1 = int(input("Enter First Number"))
        number_2 = int(input("Enter Two Number"))
        swap_number = number_1
        number_1 = number_2
        number_2 = swap_number
        print("Numbers After Swapping :")
        print("First Number : ", number_1)
        print("Second Number : ", number_2)
