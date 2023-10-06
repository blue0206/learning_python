num = [value for value in range(1, 10)]

if num:
    for value in num:
        if value == 1:
            print(f"{value}st")
        elif value == 2:
            print(f"{value}nd")
        elif value == 3:
            print(f"{value}rd")
        else:
            print(f"{value}th")
else:
    print("The list is empty!")