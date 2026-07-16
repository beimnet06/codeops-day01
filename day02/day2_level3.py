# Level 3: Advanced Tasks

# ============================================
# TASK 9: Tip Calculator (Full Program)
# ============================================
print("=" * 60)
print("TASK 9: TIP CALCULATOR")
print("=" * 60)

# Function to calculate tip
def calculate_tip(bill_amount, tip_percentage):
    """Calculate the tip amount"""
    return bill_amount * (tip_percentage / 100)

# Function to calculate total per person
def calculate_per_person(total_amount, num_people):
    """Calculate how much each person pays"""
    if num_people <= 0:
        return 0
    return total_amount / num_people

# Main tip calculator program
print("\n💰 Welcome to the Tip Calculator!")

# Get user inputs
bill = float(input("Enter the bill amount: $"))
tip_percent = float(input("Enter tip percentage (10, 15, or 20): "))
num_people = int(input("Enter number of people splitting the bill: "))

# Calculate
tip_amount = calculate_tip(bill, tip_percent)
total_amount = bill + tip_amount
per_person = calculate_per_person(total_amount, num_people)

# Display results
print("\n" + "-" * 40)
print("📊 BILL SUMMARY")
print("-" * 40)
print(f"💰 Bill amount:        ${bill:.2f}")
print(f"💵 Tip amount:         ${tip_amount:.2f}")
print(f"💲 Total amount:       ${total_amount:.2f}")
print(f"👥 Per person:         ${per_person:.2f}")
print("-" * 40)

print("\n" + "=" * 60)
print("TASK 10: SIMPLE QUIZ GAME")
print("=" * 60)

# ============================================
# TASK 10: Simple Quiz Game
# ============================================

# Function to ask a question and check answer
def ask_question(question, options, correct_answer):
    """Ask a multiple choice question and return True if correct"""
    print("\n" + question)
    for option in options:
        print(f"   {option}")
    
    answer = input("Your answer (A, B, C, or D): ").upper()
    
    if answer == correct_answer:
        print("✅ Correct! Well done!")
        return True
    else:
        print(f"❌ Wrong! The correct answer is {correct_answer}.")
        return False

# Quiz questions
print("\n🧠 Test your knowledge about Ethiopia and General Knowledge!")

# Question 1
q1 = "What is the capital of Ethiopia?"
op1 = ["A) Addis Ababa", "B) Nairobi", "C) Cairo", "D) Lagos"]
score = 0
max_score = 5

if ask_question(q1, op1, "A"):
    score += 1

# Question 2
q2 = "Which river is the longest in the world?"
op2 = ["A) Amazon", "B) Nile", "C) Mississippi", "D) Yangtze"]
if ask_question(q2, op2, "B"):
    score += 1

# Question 3
q3 = "In which year did Ethiopia join the United Nations?"
op3 = ["A) 1945", "B) 1950", "C) 1955", "D) 1960"]
if ask_question(q3, op3, "A"):
    score += 1

# Question 4
q4 = "What is the currency of Ethiopia?"
op4 = ["A) Dollar", "B) Euro", "C) Birr", "D) Shilling"]
if ask_question(q4, op4, "C"):
    score += 1

# Question 5
q5 = "Which of these is the largest ocean?"
op5 = ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"]
if ask_question(q5, op5, "D"):
    score += 1

# Display final results
print("\n" + "=" * 50)
print("📊 QUIZ RESULTS")
print("=" * 50)
print(f"✅ You got {score} out of {max_score} correct!")
print(f"📈 Percentage: {(score/max_score) * 100:.0f}%")

if score == max_score:
    print("🌟 Perfect score! You're a genius!")
elif score >= 4:
    print("👏 Excellent! You really know your stuff!")
elif score >= 3:
    print("👍 Good job! Keep learning!")
elif score >= 2:
    print("📚 Not bad! Review and try again.")
else:
    print("💪 Don't give up! Study more and try again.")

print("\n" + "=" * 60)
print("TASK 11: FUNCTION WITH DEFAULT & RETURN")
print("=" * 60)

# ============================================
# TASK 11: Function with Default & Return
# ============================================

def calculate_final_price(price, tax_rate=0.15, discount=0):
    """
    Calculate final price with tax and discount.
    
    Parameters:
    - price: Original price
    - tax_rate: Tax rate as percentage (default: 0.15 = 15%)
    - discount: Discount amount in dollars (default: 0)
    
    Returns:
    - Final price after tax and discount
    """
    # Calculate tax
    tax = price * tax_rate
    
    # Calculate price after tax
    price_with_tax = price + tax
    
    # Apply discount
    final_price = price_with_tax - discount
    
    # Ensure price doesn't go below 0
    if final_price < 0:
        final_price = 0
    
    return final_price

# Testing the function with different values
print("\n🧮 Testing calculate_final_price()\n")

# Test 1: Default values (price only)
price1 = 100
result1 = calculate_final_price(price1)
print(f"💰 Product: ${price1:.2f}")
print(f"   Default (15% tax, $0 discount): ${result1:.2f}\n")

# Test 2: Custom tax rate
price2 = 200
tax2 = 0.10
result2 = calculate_final_price(price2, tax2)
print(f"💰 Product: ${price2:.2f}")
print(f"   10% tax, $0 discount: ${result2:.2f}\n")

# Test 3: With discount
price3 = 150
tax3 = 0.15
discount3 = 20
result3 = calculate_final_price(price3, tax3, discount3)
print(f"💰 Product: ${price3:.2f}")
print(f"   15% tax, $20 discount: ${result3:.2f}\n")

# Test 4: Large discount (price becomes 0)
price4 = 50
tax4 = 0.15
discount4 = 60
result4 = calculate_final_price(price4, tax4, discount4)
print(f"💰 Product: ${price4:.2f}")
print(f"   15% tax, $60 discount: ${result4:.2f}")
print("   (Price cannot go below $0)\n")

print("\n" + "=" * 60)
print("🎉 LEVEL 3 COMPLETE!")
print("=" * 60)
