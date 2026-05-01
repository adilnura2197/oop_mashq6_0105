class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Inson ma’lumotlari")


class Student(Person):
    def __init__(self, name, age, university, course):
        super().__init__(name, age)
        self.university = university
        self.course = course

    def info(self):
        super().info()
        print(f"Ism: {self.name}")
        print(f"Universitet: {self.university}")

    def study(self):
        print(f"{self.course}-kursda o‘qiyapti")


s1 = Student("Ali", 20, "TATU", 2)

s1.info()
s1.study()
