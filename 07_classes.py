
# ------------------ 1. Class and Object Basics ------------------
class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


# Create three student objects
s1 = Student("Alice", 20, "A")
s2 = Student("Bob", 21, "B+")
s3 = Student("Charlie", 19, "A-")

s1.display_info()
s2.display_info()
s3.display_info()


# ------------------ 2. Instance vs Class Methods ------------------
class BankAccount:

    bank_name = "Guantai Jp Bank" 

    def __init__(self,account_number, balance=0):
        self.account_number =  account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(f"Account {self.account_number} Balance: {self.balance}")

    @classmethod
    def display_bank_name(cls):
        print(f"Bank Name: {cls.bank_name}")


# Create two account objects
acc1 = BankAccount("ACC123", 500)
acc2 = BankAccount("ACC456", 1000)

acc1.deposit(200)
acc1.withdraw(100)
acc1.display_balance()

acc2.withdraw(300)
acc2.deposit(500)
acc2.display_balance()

BankAccount.display_bank_name()


# ------------------ 3. Encapsulation ------------------
class Car:

    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = 0  # private attribute

    # Getter and Setter for make
    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    # Getter and Setter for model
    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    # Getter and Setter for year
    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    # Speed controls
    def accelerate(self, amount):
        self.__speed += amount

    def brake(self, amount):
        self.__speed = max(0, self.__speed - amount)

    def display_info(self):
        """Displays car details."""
        print(f"{self.__year} {self.__make} {self.__model}, Speed: {self.__speed} km/h")


# Demonstrate encapsulation
car = Car("Toyota", "Corolla", 2020)
car.display_info()
car.accelerate(50)
car.display_info()
car.brake(20)
car.display_info()
car.set_model("Camry")
car.display_info()


# ------------------ 4. Methods with Objects as Arguments ------------------
class Circle:
    """Represents a circle with radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.1416 * self.radius


class Cylinder:
    """Cylinder uses a Circle object for base area."""

    def __init__(self, circle, height):
        self.circle = circle  # Circle object
        self.height = height

    def volume(self):
        return self.circle.area() * self.height


# Demonstrate
circle = Circle(7)
print("Circle Area:", circle.area())
print("Circle Circumference:", circle.circumference())

cylinder = Cylinder(circle, 10)
print("Cylinder Volume:", cylinder.volume())


# ------------------ 5. Object Relationships (Aggregation) ------------------
class Author:

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def display_info(self):
        print(f"Author: {self.name}, Nationality: {self.nationality}")


class Book:

    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author 

    def display_info(self):
        print(f"Book: {self.title}, Price: {self.price}")
        self.author.display_info()


# Demonstrate aggregation
author = Author("George Orwell", "British")
book1 = Book("1984", 15.99, author)
book2 = Book("Animal Farm", 9.99, author)

book1.display_info()
book2.display_info()


# ------------------ 6. Assignment Challenge (Optional) ------------------
class Rectangle:
    """Represents a rectangle."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def compare_area(self, other):
        """Compares the area with another rectangle."""
        if self.area() > other.area():
            print("This rectangle is larger.")
        elif self.area() < other.area():
            print("Other rectangle is larger.")
        else:
            print("Both rectangles have equal area.")


# Demonstrate
r1 = Rectangle(10, 5)
r2 = Rectangle(8, 6)
r3 = Rectangle(10, 5)

print("Rectangle 1 Area:", r1.area())
print("Rectangle 2 Area:", r2.area())
print("Rectangle 3 Area:", r3.area())

r1.compare_area(r2)
r1.compare_area(r3)
