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

# import random

# number_to_guess = random.randint(1, 50)
# while True:
#     try:
#         guesses = int(input("Please enter the number between 1 to 100: "))
#         if guesses < number_to_guess:
#             print("Too Low!")
#         elif guesses > number_to_guess:
#             print("Too High!")
#         else:
#             print("Congratulation ! you have guessed the correct number")
#             break
#     except ValueError:
#         print("Incorrect number, Plese try again the correct number!!.")

import random

emojis = {"R": "🪨", "P": "📄", "S": "✂️"}
choices = ["R", "P", "S"]

while True:

    user_choice = input("Please choose rock, paper, scissors(r/s/p):").upper()
    if user_choice not in choices:
        print("!!!!!! Invalid choice !!!!")
        continue

    computer_choice = random.choice(choices).upper()

    print(f"You chose: {emojis[user_choice]}")
    print(f"You chose: {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Its Tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
            (user_choice == "p" and computer_choice == "r")):
        print("You Win!! ")
    else:
        print("You Lost")
    should_continue = input("Continue? (y/n)").upper()
    if should_continue == "n":
        break
