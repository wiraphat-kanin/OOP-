# __init() เป็น reserved method มีหน้าที่เป็น constructor เป็นการกำหนดค่าเริ่มต้นของ properties เเละถูกเรียกทำงานโดยอันโนมัติ เมื่อสร้าง **ออบเจ็ค**
# *** __init__() คือการประกาศ constructor
# constructor จะมีการรับ argument 1 ตัว คือ self ไว้สำหรับอ้างอิงออบเจ็คของตัวมันเอง

# การกำหนดค่าเริ่มต้นให้ properties ในเมธอด __init__()

class Mycar: # ชื่อคลาสตัวเริ่มต้นจะเป็นตัวพิมพ์ใหญ่
    def __init__(self):

        # กำหนดค่าเริ่มต้นให้ properties
        self.brand = "toyota"
        self.color = "red"

my_car = Mycar() # การสร้าง object
print(my_car.brand)
print(my_car.color)

# การรับค่าเข้ามายังเมธอด __init__() โดยงางต่อท้าย argument
class Employee:
    def __init__(self,name,salary): # รับ parameter  2 ตัว ต่อจาก argument

    # self.properties = parameter
        self.name = name
        self.salary = salary

my_emp = Employee(name="Boom",salary=30000) # การสร้าง object ของคลาส
print("Name : ",my_emp.name)
print("Salary : ",my_emp.salary)

my_emp2 = Employee("ball",400000) # การสร้าง object ของคลาส
print("Name : ",my_emp.name)
print("Salary : ",my_emp.salary)

