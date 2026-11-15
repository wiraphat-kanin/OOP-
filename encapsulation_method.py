# ตัวอย่างที่ผิด
class Person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def __display(self) :
        print(self.name)
        print(self.age)

per = Person("boom", 18)
print(per.name)

# เกิด error เรียก private method  นอกคลาส
# per.__display()

# วิธีการเเก้ไข
class Person1 :
    def __init__(self, name1, age1) :
        self.name1 = name1
        self.age1 = age1
        self.__display() # จัดการทำเเบบ นี้ใน __init__()
    def __display(self) :
        print(self.name1)
        print(self.age1)

per1 = Person1("boom", 18)
