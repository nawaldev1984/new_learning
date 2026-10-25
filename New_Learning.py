import random

while True:
    choice = input("Roll the dice(y/n): ").lower()

    if choice == "y":
        dic1 = random.randint(1, 6)
        dic2 = random.randint(1, 6)
        print(f'({dic1}, {dic2})')
    elif choice == "n":
        print('Thank you for playing!')
        break
    else:
        print("Invalid choice!")
