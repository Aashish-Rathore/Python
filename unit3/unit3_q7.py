class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Department: {self.department}")

# Example usage
manager = Manager("Charlie", 40, "M456", "Sales")
manager.display()
