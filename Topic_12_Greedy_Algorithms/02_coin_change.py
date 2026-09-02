def coin_change(coins,amount):
    coins=sorted(coins,reverse=True)
    used=[]
    for c in coins:
        while amount>=c:
            amount-=c
            used.append(c)
    return used

coins=[1, 5, 10, 25]; amount=63
used=coin_change(coins,amount)
print("Coins:",used)
print("Minimum coins:",len(used))
