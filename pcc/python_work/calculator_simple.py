print("This is a simple calculator. Enter the operation you want to carry out.")
print("\tEnter 'A' for Addition.\n\tEnter 'S' for Subtraction.")
print("\tEnter 'D' for Division.\n\tEnter 'M' for Multiplication.\n")
type = input()
type = type.lower()

print("Enter the numbers one by one you want to perform operation on.")
print("Enter 'S' to stop entering numbers.")
num = []
answer = None

while True:
    item = input()
    if item.lower() == 's':
        break
    item = int(item)
    num.append(item)

if type == 'a':
    answer = sum(num)
elif type == 's':
    value = None
    for item in num:
        if item == num[0]:
            value = item
        else:
            value -= item
    answer = value
elif type == 'd':
    value = None
    for item in num:
        if item == num[0]:
            value = item
        else:
            value /= item
    answer = value
elif type == 'm':
    value = num[0]
    for item in num:
        if item == num[0]:
            continue
        else:
            value *= item
    answer = value

print(f"The answer is {answer}")