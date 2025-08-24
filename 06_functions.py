# # 1. Write a function greet(name) that prints “Hello, [name]”.
def greet(name):
    print("Hello, " + name)

greet("Alice")


# # # 2. Create a function add(a, b) that returns the sum.
def add(a, b):
    return a + b 

print("Sum:", add(5, 3))

# # # 3. Modify add() to print “even” or “odd” based on the result.
def add_and_check(a, b):
    result = a + b
    print("Sum:", result)
    if result % 2 == 0:
        print("The result is even")
    else:
        print("The result is odd")
    return result

add_and_check(4, 7)


# # # 4. Call a function from within another function.
def square(x):
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)  # Calling square() inside another function

print("Sum of squares:", sum_of_squares(3, 4))


#  Challenge: Calculator Function
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation!"

# Example usage
print("Calculator Results:")
print("5 + 3 =", calculator(5, 3, "+"))
print("10 - 2 =", calculator(10, 2, "-"))
print("6 * 4 =", calculator(6, 4, "*"))
print("8 / 2 =", calculator(8, 2, "/"))
print("8 / 0 =", calculator(8, 0, "/"))
