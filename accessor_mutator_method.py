# accessor เมธอดรดึงค่า properties ของ object getProperties
# mutator เมธอดเเก้ไข properties ของ object setProperties

class Office:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def display(self):
        print("Name : ",self.name)
        print("Salary : ",self.__salary)

    def getSalary(self):
        print("Salary old: ",self.__salary)

    def setSalary(self,name,salary):
        if name != "boom":
            if salary < 300:
                print("Salary is less than 300")

            else:
                self.__salary = salary

        else:
            self.__salary = salary

my_name = input("Enter your name: ")
my_salary = int(input("Enter your salary: "))
my_newsalary = int(input("Enter your new salary: "))

ofc = Office(my_name,my_salary) # สร้าง object ของคลาส

ofc.display() # เเสดงค่า เมธอด display

ofc.setSalary(my_name,my_newsalary) # เเก้ไขค่าใหมให้ properties  ออบเจ็ค
ofc.getSalary() # ดึงค่า properties ของออบเจ็ค



