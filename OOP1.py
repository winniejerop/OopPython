class Employee:
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6

    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved!")
        else:
            print ("Target has not been achieved")


employeeOne = Employee()
print(employeeOne.name)

print (employeeOne.hasAchievedTarget())

print(type(employeeOne))
