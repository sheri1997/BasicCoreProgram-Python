import random


class FlipCoin:
    """this fuction we are checking if the value of
        random number is 0 then the value of tail will increse by 1
        else the value of head will be increased by 1.
        the number of times the coin will be flipped would be decided
        by the user by entering the value."""
    def flip_coin_fun(self):
        head = 0
        tail = 0
        number_flip = int(input("Enter The Number Of Times the Coin Will Flip :"))
        b = number_flip + 1
        if number_flip >= 1:
            for coin_flip in range(1, b):
                a = random.randint(0, 1)
                if a == 0:
                    tail = tail + 1
                else:
                    head = head + 1
            head_percentage = ((head / number_flip) * 100)
            tail_percentage = ((tail / number_flip) * 100)
            print("Coin Was Flipped ", number_flip, " Times")
            print("Head Came ", head, " Times")
            print("Tail Came ", tail, " Times")
            print("Head Percentage is ", head_percentage)
            print("Tail Percentage is ", tail_percentage)
        else:
            print("Please Enter A Positive Integer")

