def calculate_coins(sum):
    coins = {1: 0, 2: 0, 100: 0, 5: 0, 10: 0, 50: 0, 20: 0}
    sum *= 100
    print(sum)
    sum=int(sum)
    print(sum)
    while sum != 0:
        if sum >= 100:
            coins[100] += 1
            sum -= 100
        elif sum >= 50:
            coins[50] += 1
            sum -= 50
        elif sum >= 20:
            coins[20] += 1
            sum -= 20
        elif sum >= 10:
            coins[10] += 1
            sum -= 10
        elif sum >= 5:
            coins[5] += 1
            sum -= 5
        elif sum >= 2:
            coins[2] += 1
            sum -= 2
        elif sum >= 1:
            coins[1] += 1
            sum -= 1

    return coins
print (calculate_coins(0.28))
