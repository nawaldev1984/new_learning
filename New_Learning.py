# import random

# while True:
#     choice = input("Roll the dice(y/n): ").lower()

#     if choice == "y":
#         dic1 = random.randint(1, 6)
#         dic2 = random.randint(1, 6)
#         print(f'({dic1}, {dic2})')
#     elif choice == "n":
#         print('Thank you for playing!')
#         break
#     else:
#         print("Invalid choice!")

import random

Number_to_guess = random.randint(1, 10)
try:
    Guesses = int(input("Guess the number between 1 and 100: "))
except ValueError:
    print("Please enter a valid number")
