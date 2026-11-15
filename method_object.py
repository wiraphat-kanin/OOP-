# การสร้างเเละเรียกใช้งานเมธอด

class Employee:
    def __init__(self, emp_id , name, dept, salary):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.salary = salary

    def my_employee(self): # ยังใช้ self เพื่ออ้างอิง ออบเจ็คของตัวมันเอง
        if self.dept == "IT": # ต้องนำ self. มาอ้างอิง object ของตัวมันเอง
            print("แผนก : information technology ")
        else :
            print("แผนก : ",self.dept)

emp = Employee("001",'boom',"IT",30000) # การสร้าง object ของคลาส
emp.my_employee() # เรียกใช้ เมธอดของคลาส ที่มี print

