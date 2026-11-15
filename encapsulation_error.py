# การกำหนดระดับการใช้งานตัวเเปรเเละเมธอด เข้าใช้งานระดับ private  ได้ดังนี้ __ชื่อตัวแปร

class Office:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def display(self):
        print("Name : ",self.name)
        print("Salary : ",self.__salary)

ofc = Office("Bob",400000)
ofc.display() # ต้วนี้เนียกใช้งานได้เพราะตัวแปร self.__salary ของเมธอดนี้มันอยู่ในคลาส

# เรียกใช้ตัวแปรออกนอกคลาส __salary เลยเกิด Error
# print("Name : ",ofc.name,"Salary : "ofc.__salary)

