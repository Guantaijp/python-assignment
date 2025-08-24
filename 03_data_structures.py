# 1. Create a list of 5 fruits and print the third fruit.
fruits = ["apple", "banana", "mango", "orange", "grape"]
print("Third fruit is:", fruits[2])  # Index starts at 0
print(fruits[2])
# print(fruits.index("mango"))

# 2. Create a dictionary with keys: name, age. Print the value of age.
person = {"name": "John", "age": 25}
print("Age is:", person["age"])

# 3. Define a tuple with three numbers. Try modifying it.
numbers = (10, 20, 30)
# Uncommenting below line will throw an error
# numbers[1] = 50
print("Tuple is:", numbers)
#  Tuples are immutable → You cannot modify their elements

# 4. Create a set from a list with duplicate values.
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)
print("Unique values in the set:", unique_nums)


# Challenge
# Create a program that:
# - Takes 5 user inputs and stores them in a list
# - Converts the list into a set and prints the unique values

user_inputs = []
for i in range(5):
    value = input(f"Enter value {i+1}: ")
    user_inputs.append(value)

print("Your list:", user_inputs)

unique_values = set(user_inputs)
print("Unique values:", unique_values)
