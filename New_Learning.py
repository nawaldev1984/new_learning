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

# import random

# ROCK = "R"
# SCISSORS = "S"
# PAPER = "P"

# emojis = {ROCK: "🪨", PAPER: "📄", SCISSORS: "✂️"}
# choices = tuple(emojis.keys())


# def get_user_choice():
#     while True:
#         user_choice = input(
#             "Please choose rock, paper, scissors(r/s/p):").upper()
#         if user_choice in choices:
#             return user_choice
#         else:
#             print("!!!!!! Invalid choice !!!!")


# def desplay_choices(user_choice, computer_choice):

#     print(f"You chose: {emojis[user_choice]}")
#     print(f"Computer chose: {emojis[computer_choice]}")


# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         print("Its Tie!")
#     elif (

#         (user_choice == ROCK and computer_choice == SCISSORS) or
#         (user_choice == SCISSORS and computer_choice == PAPER) or
#             (user_choice == PAPER and computer_choice == ROCK)):
#         print("You Win!! ")
#     else:
#         print("You Lost")


# def play_game():
#     while True:
#         user_choice = get_user_choice()

#         computer_choice = random.choice(choices)

#         desplay_choices(user_choice, computer_choice)
#         determine_winner(user_choice, computer_choice)

#         should_continue = input("Continue? (y/n)").lower()
#         if should_continue == "n":
#             break


# play_game()


# QR Code builder
# ====================

