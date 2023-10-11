class Employee:
    """Give default or custom raise to an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the first name, last name, and annual salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.salary_raise = 5000
    
    def give_raise(self, salary_raise=''):
        """Gives a raise adds it to annual salary."""
        if salary_raise:
            self.salary_raise = int(salary_raise)
        self.annual_salary += self.salary_raise
    
    def display_raised_salary(self):
        """Displays the raise amount and new annual salary."""
        display = f"\nThe annual salary of {self.first_name} {self.last_name} has"
        display += f" been raised by Rs{self.salary_raise}."
        display += f"\nThe new annual salary is Rs{self.annual_salary}."
        print(display)