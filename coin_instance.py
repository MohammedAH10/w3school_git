import coin_class as cn

coin = cn.Coin()

print("This is the current side of the coin", coin.get_sideup())
print("Tossing the coin", coin.toss_coin())
print("Now this is the current side of the coin", coin.get_sideup())
