# 1. Print the type of 42, 3.14, and 'hello'.
print(type(42))       
print(type(3.14))     
print(type('hello'))  

# 2. Convert a string '100' to an integer.
num_str = '100'
num_int = int(num_str)
print(num_int, type(num_int)) 

# 3. Add an integer and a float together. What is the result?
result = 10 + 3.5
print(result, type(result))  
# ➝ When you add int + float, Python automatically promotes the int to a float.

# 4. What happens when you try to multiply a string by a number?
text = "hello"
print(text * 3)  # hellohellohello
# ➝ Python repeats the string that many times.

# Write a program that:

# Asks the user to enter two numbers (as strings)
# Converts them to integers or floats
# Prints their sum and type
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")   

# Convert to float and calculate sum
sum_result = int(num1) + int(num2)
print("The sum is:", sum_result)
print("The type of the sum is:", type(sum_result))