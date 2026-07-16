# Level 2: Intermediate Tasks

# ============================================
# Task 5: Grade Classifier
# ============================================
print("=" * 50)
print("TASK 5: GRADE CLASSIFIER")
print("=" * 50)

score = float(input("Enter your score (0-100): "))

if score >= 90 and score <= 100:
    print("🌟 Excellent!")
elif score >= 80 and score <= 89:
    print("👏 Very Good!")
elif score >= 70 and score <= 79:
    print("👍 Good!")
elif score >= 50 and score <= 69:
    print("✅ Pass")
elif score >= 0 and score < 50:
    print("❌ Fail")
else:
    print("⚠️ Invalid score! Please enter a number between 0-100.")

print("\n" + "=" * 50)
print("TASK 6: NUMBER PATTERN")
print("=" * 50)

# ============================================
# Task 6: Number Pattern
# ============================================
print("\n--- Odd Numbers from 1 to 20 ---")
for i in range(1, 21):
    if i % 2 != 0:  # Check if odd
        print(i, end=" ")
print("\n")

print("--- Numbers Divisible by 5 from 1 to 20 ---")
for i in range(1, 21):
    if i % 5 == 0:  # Check if divisible by 5
        print(i, end=" ")
print("\n")

print("--- Numbers that are Odd AND Divisible by 5 ---")
for i in range(1, 21):
    if i % 2 != 0:  # Check if odd
        if i % 5 == 0:  # Nested if: check if divisible by 5
            print(i, end=" ")
print("\n")

print("\n" + "=" * 50)
print("TASK 7: WHILE LOOP PRACTICE")
print("=" * 50)

# ============================================
# Task 7: While Loop Practice
# ============================================
total = 0
count = 0

print("Enter positive numbers to add them up.")
print("Enter 0 to stop and see the total.\n")

while True:
    num = float(input("Enter a number: "))
    
    if num == 0:
        break  # Exit the loop
    
    if num < 0:
        print("⚠️ Please enter a positive number!")
        continue  # Skip adding negative numbers
    
    total += num
    count += 1
    print(f"✅ Added {num}. Current total: {total}")

print(f"\n📊 Summary:")
print(f"   Total numbers entered: {count}")
print(f"   Sum of all numbers: {total}")

print("\n" + "=" * 50)
print("TASK 8: FUNCTION PRACTICE")
print("=" * 50)

# ============================================
# Task 8: Function Practice
# ============================================

# Function 1: greet
def greet(name):
    """Prints a welcome message"""
    print(f"👋 Welcome, {name}!")
    print(f"Hello {name}, nice to meet you!")

# Function 2: square
def square(number):
    """Returns the square of a number"""
    return number * number

# Function 3: is_even
def is_even(number):
    """Returns True if number is even, False otherwise"""
    if number % 2 == 0:
        return True
    else:
        return False

# Test the functions
print("\n--- Testing Functions ---")

# Test greet
print("\n1. Testing greet():")
greet("Beimnet")

# Test square
print("\n2. Testing square():")
num = 7
result = square(num)
print(f"   Square of {num} is {result}")

# Test is_even
print("\n3. Testing is_even():")
test_numbers = [4, 7, 10, 3, 8]
for num in test_numbers:
    if is_even(num):
        print(f"   {num} is even ✅")
    else:
        print(f"   {num} is odd ❌")

print("\n" + "=" * 50)
print("LEVEL 2 COMPLETE! 🎉")
print("=" * 50)
