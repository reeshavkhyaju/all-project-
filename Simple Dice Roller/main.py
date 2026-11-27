import random


dice_faces = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}


print("Welcome to the Dice Roller!")

# num = random.randint(1, 6)
# print(f"You rolled {num}!")

play_choice = input("Roll the dice? (y/n): ")

# while play_choice == "y":
# while play_choice.lower() == "y":
while play_choice.lower().strip() == "y":
    num = random.randint(1, 6)

    print(f"You rolled {num}!")

    # for line in dice_faces[1]:
    for line in dice_faces[num]:
        print(line)

    play_choice = input("Roll again? (y/n): ")



print("Thanks for playing! Goodbye!")









