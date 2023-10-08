print("Enter 2 numbers and get their sum.")
print("Enter 'q' to quit.")

while True:
    num1 = input("Enter First Number: ")
    if num1 == 'q':
        break
    num2 = input("Enter Second Number: ")
    if num2 == 'q':
        break
    
    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print("You have to enter a number!")
    else:
        print(f"The sum is {answer}")