from random import choice

coupon = ['4', 's', '8', 'g', '5', 'm', '2', '9', 'p', 'd' ]
lottery = choice(coupon)
for value in range(3):
    lottery += choice(coupon)
print(f"Lottery Winner is:\n{lottery}\nCongratulations on winning the lottery!")

