from FlipCoin import FlipCoin
# Added a program of Flip Coin

class BasicCore:
    def __init__(self):
        flip = FlipCoin.flip_coin_fun("Welcome")
        print(flip)


welcome = BasicCore.__init__("Welcome")
print(welcome)

