# 1. Use a for loop to print numbers from 1 to 10.
# for i in range(1, 11):
#     print(i)
# for i in range(1, 11):
#     print(i)

# # 2. Use a while loop to print numbers until the user enters 'stop'.
# while True:
#     value = input("Enter a number (or type 'stop' to quit): ")
#     if value.lower() == "stop":
#         break
#     print("You entered:", value)


# # 3. Write a loop that prints even numbers from 1 to 20.
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

for i in range(1,21):
    if i % 2 != 0:
        print(i)

# # 4. Explain what break and continue do:
# # - break: completely exits the loop, no more iterations.
# # - continue: skips the current iteration and moves to the next one.


# # Challenge: Guessing Game
import random

secret_number = random.randint(1, 10)  # Random secret number between 1 and 10
guess = None

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! The secret number was", secret_number)
