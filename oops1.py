# initiate a class 
class employee:
    # special method --constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = 'SDE'
        print("attributes/data have been initiated.")
        
    def travel(self, dest):
        print("This travel method was called manually!")
        print(f"Employee is now traveling to {dest}")

# create an instance (obj) of class employee
sam = employee()

# printing an attribute
print(sam.salary)

# calling a method 
sam.travel('Lahore')

# checking type
print(type(sam))