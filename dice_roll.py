import random

print("🎲 Welcome to Dice Roller Simulator 🎲")

while True:
    input("Press Enter to roll the dice...")
    roll = random.randint(1, 6)
    print(f"You rolled: {roll}")
    print()
    again = input("Roll again? (y/n): ").lower()
    if again != 'y':
        print("\nThanks for playing!")
        break