import random

from random import randint

amount_coin = int(input('введите количество монет: '))

m = 0
k = 0
coins = [0, 1]

for i in range(amount_coin):
    random.shuffle(coins)
    
    if int(coins[0]) == 0:
        k += 1
    if int(coins[0]) == 1:
        m += 1
        
print(f'Монет вверх гербом -> {m}')
print(f'Монет вверх режкой -> {k}')

if m > k:
    ans = k
else:
    ans = m

print(f"Минимальное количество монет, которые нужно перевернуть -> {ans}")