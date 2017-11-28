class Employee:
    def employeeDetails(self):
        self.name = "Matthew"
        print(self.name)
        self.age = 30
        print("Age= ", self.age)

    def printEmployeeDetails(self):
        print("Printing in another method")
        print("Name", self.name)
        print("Age", self.age)


employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()
