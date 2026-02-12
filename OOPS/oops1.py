class Employee:
    def __init__(self, name, employee_id, basic_salary):
        self.name = name
        self.employee_id = employee_id
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = 0.20 * self.basic_salary
        bonus = 0.10 * self.basic_salary
        total_salary = self.basic_salary + hra + bonus
        return total_salary

    def display_details(self):
        total_salary = self.calculate_salary()

        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Total Salary: {total_salary}")

emp1 = Employee("John", 101, 50000)
emp1.display_details()
