# ============================================
# Day 4 - Level 1: Classes & Objects
# ============================================

print("=" * 60)
print("TASK 1: SIMPLE CLASS - PERSON")
print("=" * 60)

# 1. Simple Class – Person
class Person:
    """A simple Person class with name and age"""
    
    def __init__(self, name, age):
        """Constructor to initialize name and age"""
        self.name = name
        self.age = age
    
    def introduce(self):
        """Method to introduce the person"""
        print(f"👋 Hello! My name is {self.name} and I am {self.age} years old.")

# Create 2 Person objects
print("\n--- Creating Person Objects ---")
person1 = Person("Beimnet Tariku", 22)
person2 = Person("Abel Kebede", 25)

# Call introduce() on both
print("\n--- Introductions ---")
person1.introduce()
person2.introduce()

print("\n" + "=" * 60)
print("TASK 2: RECTANGLE CLASS")
print("=" * 60)

# 2. Rectangle Class
class Rectangle:
    """A Rectangle class with length and width"""
    
    def __init__(self, length, width):
        """Constructor to initialize length and width"""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate and return the area"""
        return self.length * self.width
    
    def perimeter(self):
        """Calculate and return the perimeter"""
        return 2 * (self.length + self.width)

# Create 2 Rectangle objects
print("\n--- Creating Rectangle Objects ---")
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)

# Call area() and perimeter() on both
print("\n--- Rectangle 1 (10 x 5) ---")
print(f"Area: {rect1.area()}")
print(f"Perimeter: {rect1.perimeter()}")

print("\n--- Rectangle 2 (7 x 3) ---")
print(f"Area: {rect2.area()}")
print(f"Perimeter: {rect2.perimeter()}")

print("\n" + "=" * 60)
print("TASK 3: BANK ACCOUNT (BASIC)")
print("=" * 60)

# 3. Bank Account (Basic)
class Account:
    """A basic Account class with owner and balance"""
    
    def __init__(self, owner, balance=0):
        """Constructor to initialize owner and balance"""
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ${amount:.2f}")
            print(f"💰 New balance: ${self.balance:.2f}")
        else:
            print("❌ Deposit amount must be positive!")
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"✅ Withdrew ${amount:.2f}")
                print(f"💰 New balance: ${self.balance:.2f}")
            else:
                print(f"❌ Insufficient balance! You have ${self.balance:.2f}")
        else:
            print("❌ Withdrawal amount must be positive!")

# Create an account object
print("\n--- Creating Account ---")
my_account = Account("Beimnet Tariku", 1000)
print(f"Account owner: {my_account.owner}")
print(f"Initial balance: ${my_account.balance:.2f}")

# Test deposits and withdrawals
print("\n--- Testing Deposits ---")
my_account.deposit(500)

print("\n--- Testing Withdrawals ---")
my_account.withdraw(200)

print("\n--- Testing Overdraw ---")
my_account.withdraw(2000)

print("\n" + "=" * 60)
print("LEVEL 1 COMPLETE! 🎉")
print("=" * 60)
