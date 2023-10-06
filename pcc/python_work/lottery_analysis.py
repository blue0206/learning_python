from random import choice

coupon = ['4', 's', '8', 'k', '5', 'm', '2', '9', 'p', 'd' ]
times = 1
while True:
    lottery = choice(coupon)
    for value in range(3):
        lottery += choice(coupon)
    if lottery == 'd58k':
        break
    times += 1

print(f"We get '{lottery}' in {times} attempts!")