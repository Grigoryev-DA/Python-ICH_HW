class Employee:
    def __init__(self, first_name, last_name, age, employee_id, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__employee_id = employee_id
        self.__position = position
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_info(self):
        return f"Name: {self.get_full_name()}, Age: {self.age}"

    def get_employee_info(self):
        basic_info = self.get_info()
        return f"{basic_info}, Employee ID: {self.__employee_id}, Position: {self.__position}"



employee = Employee("Ivan", "Ivanov", 25, "S54321", "Computer Science")
print(employee.get_employee_info())
print(employee.get_info())

print(employee.__employee_id)