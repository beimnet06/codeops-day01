# ============================================
# Day 3 - Level 1: Basic Tasks
# ============================================

print("=" * 60)
print("TASK 1: LISTS & TUPLES")
print("=" * 60)

# 1. Lists & Tuples
print("\n--- Lists ---")

# Create a list of 6 favorite foods
favorite_foods = ["Injera", "Doro Wat", "Tibs", "Kitfo", "Shiro", "Firfir"]
print(f"My favorite foods: {favorite_foods}")

# Print the first and last food
print(f"First food: {favorite_foods[0]}")
print(f"Last food: {favorite_foods[-1]}")

# Add a new food using .append()
favorite_foods.append("Beyainatu")
print(f"After adding Beyainatu: {favorite_foods}")

# Remove the second food using .pop()
removed_food = favorite_foods.pop(1)  # Removes "Doro Wat"
print(f"Removed: {removed_food}")
print(f"After removing second food: {favorite_foods}")

# Create a tuple of coordinates for Ethiopia and unpack
ethiopia_coordinates = (8.9806, 38.7578)
latitude, longitude = ethiopia_coordinates
print(f"\n--- Tuples ---")
print(f"Ethiopia coordinates: ({latitude}, {longitude})")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

print("\n" + "=" * 60)
print("TASK 2: DICTIONARIES")
print("=" * 60)

# 2. Dictionaries
print("\n--- Dictionaries ---")

# Create a dictionary student
student = {
    "name": "Beimnet Tariku",
    "age": 22,
    "grade": "A",
    "city": "Addis Ababa",
    "department": "Computer Science"
}

print(f"Student dictionary: {student}")

# Print the student's name, department, and grade
print(f"\nStudent Name: {student['name']}")
print(f"Department: {student['department']}")
print(f"Grade: {student['grade']}")

# Add a new key phone
student["phone"] = "0910607442"
print(f"\nAfter adding phone: {student}")

# Update the grade
student["grade"] = "A+"
print(f"After updating grade: {student}")

print("\n" + "=" * 60)
print("TASK 3: SETS")
print("=" * 60)

# 3. Sets
print("\n--- Sets ---")

# Create a list with duplicate names
names_list = ["Beimnet", "Abel", "Sara", "Beimnet", "Dawit", "Sara", "Kebede"]
print(f"List with duplicates: {names_list}")

# Convert to a set to remove duplicates
names_set = set(names_list)
print(f"Set without duplicates: {names_set}")

# Add a new name to the set
names_set.add("Meron")
print(f"After adding Meron: {names_set}")

print("\n" + "=" * 60)
print("LEVEL 1 COMPLETE! 🎉")
print("=" * 60)
