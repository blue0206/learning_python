from raise_function import Employee as E

print("This program gives raise to the employee's salary.")
print("Just press enter to give default raise or enter custom amount.")

while True:
    first_name = input("Enter employee first name: ")
    last_name = input("Enter employee last name: ")
    annual_salary = input("Enter employee annual salary: ")
    annual_salary = int(annual_salary)
    employee = E(first_name, last_name, annual_salary)

    raise_amount = input("Raise Amount: ")
    if raise_amount:
        raise_amount = int(raise_amount)
        employee.give_raise(raise_amount)
    else:
        employee.give_raise()
    
    employee.display_raised_salary()

    prompt = input("Would you like to continue? (Y/N): ")
    if prompt.lower() == 'n':
        break 