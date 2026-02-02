# ------------------------------
# 1. Bank Account with private balance
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

# Example
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Current Balance:", account.get_balance())
print("-" * 40)

# 2. Student class with private attributes
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def display(self):
        print(f"Student Name: {self.__name}, Marks: {self.__marks}")

# Example
student = Student("Alice", 88)
student.display()
print("-" * 40)

# 3. Employee class with private salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def update_salary(self, new_salary):
        self.__salary = new_salary

    def display_salary(self):
        print(f"{self.name}'s Salary: {self.__salary}")

# Example
emp = Employee("Bob", 5000)
emp.display_salary()
emp.update_salary(6000)
emp.display_salary()
print("-" * 40)

# 4. Vehicle and Car classes (inheritance)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def display(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Example
my_car = Car("Toyota", "Corolla")
my_car.display()
print("-" * 40)

# 5. Person and Student classes (inheritance)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class StudentPerson(Person):
    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

# Example
s = StudentPerson("Charlie", 20)
s.display()
print("-" * 40)

# 6. Family hierarchy: Grandparent -> Parent -> Child
class Grandparent:
    def __init__(self, gp_name):
        self.gp_name = gp_name

class Parent(Grandparent):
    def __init__(self, gp_name, parent_name):
        super().__init__(gp_name)
        self.parent_name = parent_name

class Child(Parent):
    def __init__(self, gp_name, parent_name, child_name):
        super().__init__(gp_name, parent_name)
        self.child_name = child_name

    def display(self):
        print(f"Grandparent: {self.gp_name}, Parent: {self.parent_name}, Child: {self.child_name}")

# Example
child = Child("Grandpa Joe", "Dad Mike", "Sam")
child.display()
print("-" * 40)

# 7. Device -> Computer -> Laptop
class Device:
    def __init__(self, brand):
        self.brand = brand

class Computer(Device):
    pass

class Laptop(Computer):
    def display(self):
        print(f"Laptop Brand: {self.brand}")

# Example
laptop = Laptop("Dell")
laptop.display()
print("-" * 40)

# 8. Person -> Employee -> Manager
class PersonEmp:
    def __init__(self, name):
        self.name = name

class EmployeeRole(PersonEmp):
    pass

class Manager(EmployeeRole):
    def display(self):
        print(f"Manager Name: {self.name}")

# Example
mgr = Manager("Alice")
mgr.display()
print("-" * 40)

# 9. Academics + Sports -> Student
class Academics:
    def __init__(self, subject):
        self.subject = subject

class Sports:
    def __init__(self, sport_name):
        self.sport_name = sport_name

class StudentActivity(Academics, Sports):
    def display(self):
        print(f"Subject: {self.subject}, Sport: {self.sport_name}")

# Example
student = StudentActivity("Math", "Soccer")
student.display()
print("-" * 40)

# 10. Camera + MusicPlayer -> Smartphone
class Camera:
    def __init__(self, camera_feature):
        self.camera_feature = camera_feature

class MusicPlayer:
    def __init__(self, music_feature):
        self.music_feature = music_feature

class Smartphone(Camera, MusicPlayer):
    def display(self):
        print(f"Camera: {self.camera_feature}, Music: {self.music_feature}")

# Example
phone = Smartphone("108MP Camera", "MP3 Player")
phone.display()
