class Employee:
    def setNumberOfWorkingHours(self):
        self.numberofWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        # type: () -> object
        print(self.numberofWorkingHours)

class Trainee(Employee):
    def setNumberofWorkingHours(self):
        self.numberofWorkingHours = 45

    def resetNumberofWorkingHours(self):
        super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()
print("working hours employee")
employee.displayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberofWorkingHours()
print("working hours trainee")
trainee.displayNumberOfWorkingHours()
trainee.resetNumberofWorkingHours()

print("working hours trainee after reset")
trainee.displayNumberOfWorkingHours()